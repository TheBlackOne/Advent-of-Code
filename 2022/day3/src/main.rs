use std::fs::{File};
use std::io::{self, BufRead};
use std::collections::HashSet;

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

fn get_priority(item: &char) -> u32 {
    let offset = if item.is_lowercase() {96} else {38};
    return *item as u32 - offset;
}

fn part1(input: &Vec<String>) {
    let mut priorities_sum: u32 = 0;

    for line in input {
        let length = line.len();
        let (compartment1, compartment2) = line.split_at(length / 2);
        //println!("Compartment 1: {}, compartment 2: {}", compartment1, compartment2);
        let items1: Vec<_> = compartment1.chars().collect();
        let items2: Vec<_> = compartment2.chars().collect();

        let set1: HashSet<_> = items1.into_iter().collect();
        let set2: HashSet<_> = items2.into_iter().collect();    
        let set_common = set1.intersection(&set2);

        for common_item in set_common {
            //println!("{}", common_item)
            priorities_sum += get_priority(common_item);
        }

        //println!("Priority of item {}: {}", 'z', get_priority(&'z'));
    }

    println!("Part 1: Sum of priorities: {}", priorities_sum);
}

fn part2(input: &Vec<String>) {
    let mut priorities_sum: u32 = 0;

    for triple in input.chunks(3) {
        let items1: HashSet<_> = triple[0].chars().into_iter().collect();
        let items2: HashSet<_> = triple[1].chars().into_iter().collect();
        let items3: HashSet<_> = triple[2].chars().into_iter().collect();

        let common_a: HashSet<_> = items1.intersection(&items2).into_iter().collect();
        let common_b: HashSet<_> = items1.intersection(&items3).into_iter().collect();
        let common_c: HashSet<_> = items2.intersection(&items3).into_iter().collect();

        let common_1: HashSet<_> = common_a.intersection(&common_b).into_iter().collect();
        let common_2: HashSet<_> = common_a.intersection(&common_c).into_iter().collect();
        let common_3: HashSet<_> = common_b.intersection(&common_c).into_iter().collect();

        priorities_sum += get_priority(&common_1.iter().next().unwrap());
    }

    println!("Part 2: Sum of priorities: {}", priorities_sum);
}

fn main() {
    let input = read_input("input.txt");

    part2(&input);
}
