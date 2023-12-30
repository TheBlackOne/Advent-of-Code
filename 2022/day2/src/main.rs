use std::fs::{File};
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

#[derive(Debug, PartialEq, Eq, Copy, Clone)]
enum Choice {
    Invalid,
    Rock,
    Paper,
    Scissors
}
#[derive(Debug)]
enum RoundResult {
    Invalid,
    Loss,
    Draw,
    Win
}

fn get_choice_score(score: &Choice) -> u32 {
    match *score {
        Choice::Invalid => 0,
        Choice::Rock => 1,
        Choice::Paper => 2,
        Choice::Scissors => 3
    }
}

fn get_matchresult_score(score: &RoundResult) -> u32 {
    match *score {
        RoundResult::Invalid => 99999999,
        RoundResult::Loss => 0,
        RoundResult::Draw => 3,
        RoundResult::Win => 6
    }
}

fn parse_choice(input: char) -> Choice {
    match input {
        'A' | 'X' => Choice::Rock,
        'B' | 'Y' => Choice::Paper,
        'C' | 'Z' => Choice::Scissors,
        _ => Choice::Invalid
    }
}

fn parse_round_result(input: char) -> RoundResult {
    match input {
        'X' => RoundResult::Loss,
        'Y' => RoundResult::Draw,
        'Z' => RoundResult::Win,
        _ => RoundResult::Invalid
    }
}

fn get_choice2(choice1: &Choice, round_result: &RoundResult) -> Choice {
    match *round_result {
        RoundResult::Draw => *choice1,
        RoundResult::Win => {
            match *choice1 {
                Choice::Rock => Choice::Paper,
                Choice::Paper => Choice::Scissors,
                Choice::Scissors => Choice::Rock,
                Choice::Invalid => Choice::Invalid
            }
        },
        RoundResult::Loss => {
            match *choice1 {
                Choice::Rock => Choice::Scissors,
                Choice::Paper => Choice::Rock,
                Choice::Scissors => Choice::Paper,
                Choice::Invalid => Choice::Invalid
            }
        }
        RoundResult::Invalid => Choice::Invalid
    }
}

fn get_round_result(choice1: &Choice, choice2: &Choice) -> RoundResult {
    if *choice1 == *choice2 {
        return RoundResult::Draw;
    }

    if (*choice2 == Choice::Paper && *choice1 == Choice::Rock)
    || (*choice2 == Choice::Scissors && *choice1 == Choice::Paper)
    || (*choice2 == Choice::Rock && *choice1 == Choice::Scissors) {
        return RoundResult::Win
    }

    return RoundResult::Loss;
}

fn part2(input: &Vec<String>) {
    let mut total_score: u32 = 0;

    for line in input {
        let choice1 = parse_choice(line.chars().next().unwrap());
        let round_result = parse_round_result(line.chars().last().unwrap());
        let choice2 = get_choice2(&choice1, &round_result);

        let round_score = get_choice_score(&choice2) + get_matchresult_score(&round_result);
        total_score += round_score;}

    println!("Part 2: Total score: {}", total_score);
}

fn part1(input: &Vec<String>) {
    let mut total_score: u32 = 0;

    for line in input {
        let choice1 = parse_choice(line.chars().next().unwrap());
        let choice2 = parse_choice(line.chars().last().unwrap());

        let round_result = get_round_result(&choice1, &choice2);
        let round_score = get_choice_score(&choice2) + get_matchresult_score(&round_result);
        total_score += round_score;

        //println!("choice1: {:?}, choice2: {:?} round result: {:?}, round score: {}", choice1, choice2, round_result, round_score);
    }

    println!("Part1: Total score: {}", total_score);
}

fn main() {
    let input = read_input("input.txt");

    part1(&input);
    part2(&input);
}