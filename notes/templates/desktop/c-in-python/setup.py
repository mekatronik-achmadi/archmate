from distutils.core import setup,Extension

setup(name='helloModule',
      version="1.0",
      ext_modules=[
          Extension('helloModule',
                    ['printhello.c'])
      ])
