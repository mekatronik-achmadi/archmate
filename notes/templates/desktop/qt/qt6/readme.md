# Qt C++

Create build folder and Makefile

```sh
mkdir -p build/
cd build/

qmake6 ../
```

to also check using CLazy

```sh
qmake6 ../ \
-spec linux-clang \
QMAKE_CXX="clazy"
```

**Notes:** As CLazy were developed for Qt5,
it will show a lot of warnings.

Generate compile_commands.json

```sh
bear -- make
cp -vf compile_commands.json ../
```

Clean and build binary

```sh
make Clean
make all
```

Run the binary

```sh
./gui
```

