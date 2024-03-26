# Call C++ from Python

Compile Test C++ module

```sh
mkdir -p build/
bear -- g++ -o build/pwr.o -c pwr.cpp
```

Build and Setup CPython module

```sh
python setup.py build_ext --inplace
```

Test CPython

```sh
python -c 'import powerCalc; print(powerCalc.pwr_calc(4,3))'
```

