# Build Notes

## C Program

```sh
mkdir -p target/
g++ -o target/pwr src/main.cpp src/pwr.cpp

./target/pwr
```

## Rust Program

```sh
cargo clean
cargo build --release

cargo run
```
