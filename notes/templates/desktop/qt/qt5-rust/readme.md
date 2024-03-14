# Qt5 in Rust

## Install packages

```sh
sudo pacman -S qt5-base cmake
```

## Dependencies

Necessary dependencies to add in **Cargo.toml**

```
[dependencies]
cxx = "*"
cxx-qt = "*"
cxx-qt-lib = "*"

[build-dependencies]
cxx-qt-build = "*"
```

Test and install dependencies by build it:

```sh
cargo build --release
```

