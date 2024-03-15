# Build C++ in C

Generate Makefile

```sh
mkdir -p build/
cd build/

cmake ../
```

Generate compile_commands.json

```sh
bear -- make
mv compile_commands.json ../
```

Compile and Run

```sh
make clean
make

./main
```

