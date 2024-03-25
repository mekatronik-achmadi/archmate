# Rust FLTK

Install FLTK crate

```sh
cargo add fltk
```

**TIPS:**
Restart vim after FLTK crate installed and this line added to **main.rs**:

```rust
extern crate fltk;
```

Clean and Build binary

```sh
cargo clean

cargo build --release
```

Run binary

```
cargo run --release
```

or Run without Cargo

```sh
./target/release/fltk_template
```

