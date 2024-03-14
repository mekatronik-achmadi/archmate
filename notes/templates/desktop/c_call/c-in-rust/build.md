# Build Notes

## C Program

```sh
mkdir -p target/
gcc -o target/pwr src/main.c src/pwr.c -lm

./target/pwr
```

## Rust Program

```sh
cargo clean
cargo build --release

cargo run --release
```

## Alternative

Use [BindGen](https://github.com/rust-lang/rust-bindgen)

```sh
sudo pacman -S rust-bindgen
```
