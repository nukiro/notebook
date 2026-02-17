use std::env;
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;

pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &'static str> {
        // Validate that there are enough arguments provided
        if args.len() < 3 {
            return Err("Not enough arguments. Usage: <search_string> <input_file>");
        }

        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

        // Ignore extra arguments passed by
        // Arguments will be cloned to create owned String instances for the Config struct
        Ok(Config {
            query: args[1].clone(),
            filename: args[2].clone(),
            case_sensitive,
        })
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    // Open the file specified in the config
    let mut f = File::open(config.filename)?;
    // Read the content
    let mut contents = String::new();
    f.read_to_string(&mut contents)?;
    // Search for the query in the contents and print matching lines
    // by the search mode specified in the config
    let found = if config.case_sensitive {
        search_case_sensitive(&config.query, &contents)
    } else {
        search_case_insensitive(&config.query, &contents)
    };

    for line in found {
        println!("{}", line);
    }

    Ok(())
}

pub fn search_case_insensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.to_lowercase().contains(query.to_lowercase().as_str()))
        .collect()
}

pub fn search_case_sensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let q = query.to_lowercase();
    contents.lines().filter(|line| line.contains(&q)).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_config_new_valid_args() {
        let args = vec![
            String::from("program_name"),
            String::from("search_string"),
            String::from("input_file.txt"),
        ];
        let config = Config::new(&args).unwrap();
        assert_eq!(config.query, "search_string");
        assert_eq!(config.filename, "input_file.txt");
    }

    #[test]
    fn test_config_new_insufficient_args() {
        let args = vec![String::from("program_name")];
        let result = Config::new(&args);
        assert!(result.is_err());
    }

    #[test]
    fn test_search_case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";
        assert_eq!(
            vec!["safe, fast, productive."],
            search_case_sensitive(query, contents)
        );
    }

    #[test]
    fn test_search_case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";
        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
