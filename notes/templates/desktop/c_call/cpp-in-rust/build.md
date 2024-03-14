# Build Notes

## C Program

```sh
mkdir -p target/
g++ -o target/pwr src/main.cpp src/pwr.cpp

./target/pwr
```

## Rust Compiling

compile the C++ as linking library

```sh
g++ -c -std=c++11 -o pwr.o src/pwr.cpp
ar rcs libpwr.a pwr.o
```

run Cargo to build Rust Binary

```sh
cargo clean
cargo build --release
```

## Rust running

create shared object

```
g++ -shared -fPIC -o libpwr.so src/pwr.cpp
cp libpwr.so target/release/
```

Run the binary using command:

```sh
cargo run --release
```

