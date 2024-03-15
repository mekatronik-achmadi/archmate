# Build C++ in C

Generate Makefile

```sh
cmake -B build

mv build/compile_commands.json ../
```

Compile and Run

```sh
cmake --build build

./build/main
```

