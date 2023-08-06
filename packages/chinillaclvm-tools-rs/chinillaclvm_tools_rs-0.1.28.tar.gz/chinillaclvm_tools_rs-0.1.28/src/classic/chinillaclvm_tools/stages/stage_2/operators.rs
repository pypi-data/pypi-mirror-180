use std::cell::{Ref, RefCell};
use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;
use std::rc::Rc;

use chinillaclvm_rs::allocator::{Allocator, NodePtr, SExp};
use chinillaclvm_rs::chinilla_dialect::{ChinillaDialect, NO_NEG_DIV, NO_UNKNOWN_OPS};
use chinillaclvm_rs::cost::Cost;
use chinillaclvm_rs::dialect::Dialect;
use chinillaclvm_rs::reduction::{EvalErr, Reduction, Response};
use chinillaclvm_rs::run_program::run_program;

use crate::classic::chinillaclvm::__type_compatibility__::{Bytes, BytesFromType, Stream};

use crate::classic::chinillaclvm::keyword_from_atom;
use crate::classic::chinillaclvm::sexp::proper_list;

use crate::classic::chinillaclvm_tools::binutils::{assemble_from_ir, disassemble_to_ir_with_kw};
use crate::classic::chinillaclvm_tools::ir::reader::read_ir;
use crate::classic::chinillaclvm_tools::ir::writer::write_ir_to_stream;
use crate::classic::chinillaclvm_tools::sha256tree::TreeHash;
use crate::classic::chinillaclvm_tools::stages::stage_0::{
    DefaultProgramRunner, RunProgramOption, TRunProgram,
};
use crate::classic::chinillaclvm_tools::stages::stage_2::compile::do_com_prog_for_dialect;
use crate::classic::chinillaclvm_tools::stages::stage_2::optimize::do_optimize;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum AllocatorRefOrTreeHash {
    AllocatorRef(NodePtr),
    TreeHash(TreeHash),
}

impl AllocatorRefOrTreeHash {
    pub fn new_from_nodeptr(n: NodePtr) -> Self {
        AllocatorRefOrTreeHash::AllocatorRef(n)
    }

    pub fn new_from_sexp(allocator: &mut Allocator, n: NodePtr) -> Self {
        AllocatorRefOrTreeHash::TreeHash(TreeHash::new_from_sexp(allocator, n))
    }
}

pub struct CompilerOperators {
    base_dialect: Rc<dyn Dialect>,
    search_paths: Vec<String>,
    compile_outcomes: RefCell<HashMap<String, String>>,
    dialect: RefCell<Rc<dyn Dialect>>,
    runner: RefCell<Rc<dyn TRunProgram>>,
    opt_memo: RefCell<HashMap<AllocatorRefOrTreeHash, NodePtr>>,
}

impl CompilerOperators {
    pub fn new(search_paths: Vec<String>) -> Self {
        let base_dialect = Rc::new(ChinillaDialect::new(NO_NEG_DIV | NO_UNKNOWN_OPS));
        let base_runner = Rc::new(DefaultProgramRunner::new());
        CompilerOperators {
            base_dialect: base_dialect.clone(),
            search_paths,
            compile_outcomes: RefCell::new(HashMap::new()),
            dialect: RefCell::new(base_dialect),
            runner: RefCell::new(base_runner),
            opt_memo: RefCell::new(HashMap::new()),
        }
    }

    fn set_runner(&self, runner: Rc<dyn TRunProgram>) {
        self.runner.replace(runner);
    }

    fn set_dialect(&self, dialect: Rc<dyn Dialect>) {
        self.dialect.replace(dialect);
    }

    fn get_runner(&self) -> Rc<dyn TRunProgram> {
        let borrow: Ref<'_, Rc<dyn TRunProgram>> = self.runner.borrow();
        borrow.clone()
    }

    fn read(&self, allocator: &mut Allocator, sexp: NodePtr) -> Response {
        match allocator.sexp(sexp) {
            SExp::Pair(f, _) => match allocator.sexp(f) {
                SExp::Atom(b) => {
                    let filename =
                        Bytes::new(Some(BytesFromType::Raw(allocator.buf(&b).to_vec()))).decode();
                    fs::read_to_string(filename)
                        .map_err(|_| EvalErr(allocator.null(), "Failed to read file".to_string()))
                        .and_then(|content| {
                            read_ir(&content)
                                .map_err(|e| EvalErr(allocator.null(), e))
                                .and_then(|ir| {
                                    assemble_from_ir(allocator, Rc::new(ir))
                                        .map(|ir_sexp| Reduction(1, ir_sexp))
                                })
                        })
                }
                _ => Err(EvalErr(
                    allocator.null(),
                    "filename is not an atom".to_string(),
                )),
            },
            _ => Err(EvalErr(
                allocator.null(),
                "given a program that is an atom".to_string(),
            )),
        }
    }

    fn write(&self, allocator: &mut Allocator, sexp: NodePtr) -> Response {
        if let SExp::Pair(filename_sexp, r) = allocator.sexp(sexp) {
            if let SExp::Pair(data, _) = allocator.sexp(r) {
                if let SExp::Atom(filename_buf) = allocator.sexp(filename_sexp) {
                    let filename_buf = allocator.buf(&filename_buf);
                    let filename_bytes =
                        Bytes::new(Some(BytesFromType::Raw(filename_buf.to_vec())));
                    let ir = disassemble_to_ir_with_kw(allocator, data, keyword_from_atom(), true);
                    let mut stream = Stream::new(None);
                    write_ir_to_stream(Rc::new(ir), &mut stream);
                    return fs::write(filename_bytes.decode(), stream.get_value().decode())
                        .map_err(|_| {
                            EvalErr(sexp, format!("failed to write {}", filename_bytes.decode()))
                        })
                        .map(|_| Reduction(1, allocator.null()));
                }
            }
        }

        Err(EvalErr(sexp, "failed to write data".to_string()))
    }

    fn get_full_path_for_filename(&self, allocator: &mut Allocator, sexp: NodePtr) -> Response {
        if let SExp::Pair(l, _r) = allocator.sexp(sexp) {
            if let SExp::Atom(b) = allocator.sexp(l) {
                let filename =
                    Bytes::new(Some(BytesFromType::Raw(allocator.buf(&b).to_vec()))).decode();
                for path in &self.search_paths {
                    let mut path_buf = PathBuf::new();
                    path_buf.push(path);
                    path_buf.push(filename.clone());
                    let f_path = path_buf.as_path();
                    if f_path.exists() {
                        return f_path
                            .to_str()
                            .map(Ok)
                            .unwrap_or_else(|| {
                                Err(EvalErr(sexp, "could not compute absolute path".to_string()))
                            })
                            .and_then(|p| {
                                allocator
                                    .new_atom(p.as_bytes())
                                    .map(|res| Reduction(1, res))
                            });
                    }
                }
            }
        }

        Err(EvalErr(sexp, "can't open file".to_string()))
    }

    pub fn set_symbol_table(
        &self,
        allocator: &mut Allocator,
        table: NodePtr,
    ) -> Result<Reduction, EvalErr> {
        if let Some(symtable) =
            proper_list(allocator, table, true).and_then(|t| proper_list(allocator, t[0], true))
        {
            for kv in symtable.iter() {
                if let SExp::Pair(hash, name) = allocator.sexp(*kv) {
                    if let (SExp::Atom(hash), SExp::Atom(name)) =
                        (allocator.sexp(hash), allocator.sexp(name))
                    {
                        let hash_text =
                            Bytes::new(Some(BytesFromType::Raw(allocator.buf(&hash).to_vec())))
                                .decode();
                        let name_text =
                            Bytes::new(Some(BytesFromType::Raw(allocator.buf(&name).to_vec())))
                                .decode();

                        self.compile_outcomes.replace_with(|co| {
                            let mut result = co.clone();
                            result.insert(hash_text, name_text);
                            result
                        });
                    }
                }
            }
        }

        Ok(Reduction(1, allocator.null()))
    }
}

impl Dialect for CompilerOperators {
    fn val_stack_limit(&self) -> usize {
        todo!()
    }
    fn quote_kw(&self) -> &[u8] {
        &[1]
    }
    fn apply_kw(&self) -> &[u8] {
        &[2]
    }

    fn op(
        &self,
        allocator: &mut Allocator,
        op: NodePtr,
        sexp: NodePtr,
        max_cost: Cost,
    ) -> Response {
        match allocator.sexp(op) {
            SExp::Atom(opname) => {
                let opbuf = allocator.buf(&opname);
                if opbuf == "_read".as_bytes() {
                    self.read(allocator, sexp)
                } else if opbuf == "_write".as_bytes() {
                    self.write(allocator, sexp)
                } else if opbuf == "com".as_bytes() {
                    do_com_prog_for_dialect(self.get_runner(), allocator, sexp)
                } else if opbuf == "opt".as_bytes() {
                    do_optimize(self.get_runner(), allocator, &self.opt_memo, sexp)
                } else if opbuf == "_set_symbol_table".as_bytes() {
                    self.set_symbol_table(allocator, sexp)
                } else if opbuf == "_full_path_for_name".as_bytes() {
                    self.get_full_path_for_filename(allocator, sexp)
                } else {
                    self.base_dialect.op(allocator, op, sexp, max_cost)
                }
            }
            _ => self.base_dialect.op(allocator, op, sexp, max_cost),
        }
    }
}

impl CompilerOperators {
    pub fn get_compiles(&self) -> HashMap<String, String> {
        return self.compile_outcomes.borrow().clone();
    }
}

impl TRunProgram for CompilerOperators {
    fn run_program(
        &self,
        allocator: &mut Allocator,
        program: NodePtr,
        args: NodePtr,
        option: Option<RunProgramOption>,
    ) -> Response {
        let max_cost = option.as_ref().and_then(|o| o.max_cost).unwrap_or(0);
        run_program(
            allocator,
            self,
            program,
            args,
            max_cost,
            option.and_then(|o| o.pre_eval_f),
        )
    }
}

pub fn run_program_for_search_paths(search_paths: &[String]) -> Rc<CompilerOperators> {
    let ops = Rc::new(CompilerOperators::new(search_paths.to_vec()));
    ops.set_dialect(ops.clone());
    ops.set_runner(ops.clone());
    ops
}
