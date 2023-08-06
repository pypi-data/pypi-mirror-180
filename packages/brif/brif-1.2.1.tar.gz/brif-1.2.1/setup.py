from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import platform

if platform.system() == 'Windows':
    extra_flags = ['/openmp']
elif platform.system() != 'Darwin':
    extra_flags = ['-fopenmp']
else:
    extra_flags = ['']

setup(name='brif',
      version="1.2.1",
      ext_modules=[
          Extension('brifc',
                    ['pybrif.c','brif.c'],
                    extra_compile_args = extra_flags
                    )
          ]
      )
