#!/bin/bash

mkdir -p build/
bear -- gcc -o build/pwr.o -c pwr.c

# mkdir -p PyEnv/;cd PyEnv/
# virtualenv pwrcalc --system-site-packages
# cd ../

# source PyEnv/pwrcalc/bin/activate

# python setup.py build
# python setup.py install

python setup.py build_ext --inplace

python -c 'import powerCalc; print(powerCalc.pwr_calc(4,3))'
