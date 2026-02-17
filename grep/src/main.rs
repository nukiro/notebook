extern crate grep;
use grep::Config;
use std::env;
use std::process;

fn main() {
    // Collect command-line arguments into a vector
    let args: Vec<String> = env::args().collect();

    let config = match Config::new(&args) {
        Ok(config) => config,
        Err(error) => {
            eprintln!("Error parsing arguments: {}", error);
            process::exit(1);
        }
    };

    if let Err(e) = grep::run(config) {
        eprintln!("Application error: {}", e);
        process::exit(1);
    }
}
