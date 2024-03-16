# Build C++ in C

Generate Makefile

```sh
cmake -B build

mv build/compile_commands.json ../
```

To use memleak checker

```sh
unset LD_PRELOAD
```

Compile and Run

```sh
cmake --build build

./build/main
```

