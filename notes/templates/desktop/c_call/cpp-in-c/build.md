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

Debug using Valgrind

```sh
cmake -B debug -DCMAKE_BUILD_TYPE=Debug
cmake --build debug
ctest -T memcheck --test-dir debug
```

