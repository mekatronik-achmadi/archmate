# WASM Rust

## Install

```sh
sudo pacman -S nodejs npm rust-wasm wasm-bindgen wasm-pack
```

## New Project

```sh
cargo new wasm-basic --lib

cd wasm-basic/
```

add command line to add library:

```sh
cargo add wasm-bindgen

echo '
[lib]
crate-type = ["cdylib"]
' | tee -a Cargo.toml
```

## Compile WASM package

Build using WASM-Pack tool (requires internet to download modules)

```sh
wasm-pack build
```

## Run using webpack

First, install NPM modules

```sh
npm install
```

Run using command:

```
npm run serve
```

Open in webbrowser

```sh
firefox http://localhost:8080/
```




