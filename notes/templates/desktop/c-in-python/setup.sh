#!/bin/bash

mkdir -p build/
bear -- gcc -o build/printhello.o -c printhello.c

mkdir -p PyEnv/;cd PyEnv/
virtualenv printhello --system-site-packages
cd ../

source PyEnv/printhello/bin/activate

python setup.py build
python setup.py install

python -c 'import helloModule; helloModule.printhello()'
