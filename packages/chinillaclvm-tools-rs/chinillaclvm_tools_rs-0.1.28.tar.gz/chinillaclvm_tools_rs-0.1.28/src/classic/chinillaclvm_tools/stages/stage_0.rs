use chinillaclvm_rs::allocator::{Allocator, NodePtr};
use chinillaclvm_rs::chinilla_dialect::{ChinillaDialect, NO_NEG_DIV, NO_UNKNOWN_OPS};
use chinillaclvm_rs::cost::Cost;
use chinillaclvm_rs::reduction::Response;

use chinillaclvm_rs::run_program::{run_program, PreEval};

pub struct RunProgramOption {
    pub max_cost: Option<Cost>,
    pub pre_eval_f: Option<PreEval>,
    pub strict: bool,
}

pub trait TRunProgram {
    fn run_program(
        &self,
        allocator: &mut Allocator,
        program: NodePtr,
        args: NodePtr,
        option: Option<RunProgramOption>,
    ) -> Response;
}

pub struct DefaultProgramRunner {}

impl DefaultProgramRunner {
    pub fn new() -> Self {
        DefaultProgramRunner {}
    }
}

impl Default for DefaultProgramRunner {
    fn default() -> Self {
        DefaultProgramRunner::new()
    }
}

impl TRunProgram for DefaultProgramRunner {
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
            &ChinillaDialect::new(NO_NEG_DIV | NO_UNKNOWN_OPS),
            program,
            args,
            max_cost,
            option.and_then(|o| o.pre_eval_f),
        )
    }
}
