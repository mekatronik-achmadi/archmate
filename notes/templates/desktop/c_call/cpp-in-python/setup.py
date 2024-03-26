from distutils.core import setup,Extension

setup(name='powerCalc',
      version='1.0',
      ext_modules=[
          Extension('powerCalc',
                    ['pwr.cpp'])
          ])

