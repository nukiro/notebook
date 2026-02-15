extern crate rand;

use rand::RngExt;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!(">>> Guess the number <<<");

    let secret_number = rand::rng().random_range(0..=100);
    println!("Secret number: {}", secret_number);

    loop {
        println!("Please input your guess: ");

        let mut guess = String::new();

        match io::stdin().read_line(&mut guess) {
            Ok(s) => {
                println!("Size written: {}", s);
                s
            }
            Err(_) => {
                println!("Failed to read line");
                return;
            }
        };

        let guess: i32 = match guess.trim().parse() {
            Ok(n) => n,
            Err(_) => {
                println!("Please input a number!");
                // let's give the user another chance to input a number instead of quitting the game
                continue;
            }
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win");
                break;
            }
        }

        println!("Let's give you another chance....");
    }

    println!("The game ends... See you next time!");
}
