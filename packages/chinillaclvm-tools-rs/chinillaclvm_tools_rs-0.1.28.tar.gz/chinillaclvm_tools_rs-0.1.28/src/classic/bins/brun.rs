use chinillaclvm_tools_rs::classic::chinillaclvm_tools::cmds::brun;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    brun(&args);
}
