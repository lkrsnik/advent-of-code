use std::env;
use std::fs;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path = parse_config(&args);
    let (mut vect1, mut vect2) = read(&file_path);
    vect1.sort();
    vect2.sort();
    let distance: Vec<i32> = vect1
        .iter()
        .zip(vect2.iter())
        .map(|(x, y)| (x - y).abs())
        .collect();
    let cumulative_distance: i32 = distance.iter().sum();
    println!("{cumulative_distance}");
    // dbg!(&cumulative_distance);

    // PART 2:
    // count frequencies
    let frequencies = vect2
        .iter()
        .copied()
        .fold(HashMap::new(), |mut map, val|{
            map.entry(val)
               .and_modify(|frq|*frq+=1)
               .or_insert(1);
            map
        });
    let similarity_score: Vec<i32> = vect1
        .iter()
        .map(|x| x*frequencies.get(x).unwrap_or(&0))
        .collect();

    let cumulative_similarity_score: i32 = similarity_score.iter().sum();
    println!("{cumulative_similarity_score}");
}

fn parse_config(args: &[String]) -> &str {
    let file_path = &args[1];

    file_path
}

fn read(file_path: &str) -> (Vec<i32>, Vec<i32>) {
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut vect1: Vec<i32> = Vec::new();
    let mut vect2: Vec<i32> = Vec::new();

    let parts: Vec<_> = contents.split_whitespace().collect();
    let mut first_row = true;
    
    for part in parts {
        let my_int = part.parse::<i32>().unwrap();
        if first_row {
            vect1.push(my_int);
        } else {
            vect2.push(my_int);
        }
        first_row = !first_row;
    }
    (vect1, vect2)
}