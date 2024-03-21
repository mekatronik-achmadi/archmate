# LLVM comparisson

## Compile and IR in C

generate LLVM IR and Assembly

```sh
clang -S -emit-llvm main_c.c
clang -S -o main_c.s main_c.c
```

check generated files

```sh
bat main_c.ll
bat main_c.s
```

compile to binary

```sh
clang -o bin_main_c main_c.c
```

run the binary

```sh
./bin_main_c
```

## Compile and Assembly in C (GCC)

generate Assembly

```sh
gcc -c -S -o main_c_gcc.s main_c.c
```

check generated files

```sh
bat main_c_gcc.s
```

compile to binary

```sh
gcc -o bin_main_c_gcc main_c.c
```

run the binary

```sh
./bin_main_c_gcc
```

## Compile and IR in C++

generate LLVM IR and Assembly

```sh
clang++ -S -emit-llvm main_cpp.cpp
clang++ -S -o main_cpp.s main_cpp.cpp
```

check generated files

```sh
bat main_cpp.ll
bat main_cpp.s
```

compile to binary

```sh
clang++ -o bin_main_cpp main_cpp.cpp
```

run the binary

```sh
./bin_main_cpp
```

## Compile and IR in Rust

generate LLVM IR and Assembly

```sh
rustc --emit=llvm-ir main_rs.rs
rustc --emit=asm main_rs.rs
```

check LLVM IR

```sh
bat main_rs.ll
bat main_rs.s
```

compile source to binary

```sh
rustc -o bin_main_rs main_rs.rs
```

run the binary

```sh
./bin_main_rs
```

