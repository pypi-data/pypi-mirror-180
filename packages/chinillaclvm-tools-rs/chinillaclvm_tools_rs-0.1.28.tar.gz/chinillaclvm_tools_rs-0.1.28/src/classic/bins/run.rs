use chinillaclvm_tools_rs::classic::chinillaclvm_tools::cmds::run;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    run(&args);
}
