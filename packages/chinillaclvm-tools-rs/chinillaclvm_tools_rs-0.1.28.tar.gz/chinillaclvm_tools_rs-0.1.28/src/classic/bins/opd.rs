use chinillaclvm_tools_rs::classic::chinillaclvm_tools::cmds::opd;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    opd(&args);
}
