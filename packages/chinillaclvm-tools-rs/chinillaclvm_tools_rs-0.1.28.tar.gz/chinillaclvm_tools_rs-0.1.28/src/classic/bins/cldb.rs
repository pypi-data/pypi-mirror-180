use chinillaclvm_tools_rs::classic::chinillaclvm_tools::cmds::cldb;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    cldb(&args);
}
