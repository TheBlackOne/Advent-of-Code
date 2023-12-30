use std::fs::File;
use std::io::{self, BufRead};

fn lines_from_file(filename: &str) -> io::Result<io::Lines<io::BufReader<File>>>
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn read_input(filename: &str) -> Vec<String> {
    let mut result = Vec::<String>::new();
    let lines = lines_from_file(filename).unwrap();

    for line in lines {
        result.push(line.unwrap());
    }

    return result;
}

fn main() {
    let input = read_input("input.txt");

    let mut sum_calories: u32 = 0;
    let mut all_sums = Vec::<u32>::new();

    for line in input {
        if !line.is_empty() {
            sum_calories += line.parse::<u32>().unwrap();
        } else {
            all_sums.push(sum_calories);
            sum_calories = 0;
        }
    }

    all_sums.push(sum_calories);
    all_sums.sort();
    all_sums.reverse();

    println!("Part 1: Max calories: {}", all_sums.first().unwrap());

    let top_three = &all_sums[0..3];

    println!("Part 2: Sum of top 3 calories: {}", top_three.iter().sum::<u32>());
}
