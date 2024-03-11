fn main() {
    let mut msg_str = String::new();

    msg_str.push_str("Rust Template");
    show_msg(msg_str);
}

fn show_msg(msg: String){
    println!("Message: {}",msg);
}
