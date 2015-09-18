#!/usr/bin/env python

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

VERSION = (0, 0, 3, 1)
VERSION_STR = ".".join([str(x) for x in VERSION])

COPT =  {'msvc': ['/Ox', '/Izstd\\lib', '/DVERSION=\"\\\"%s\\\"\"' % VERSION_STR],
     'mingw32' : ['-O3', '-Izstd/lib', '-march=native', '-DVERSION="%s"' % VERSION_STR],
     'clang' : ['-O3', '-Izstd/lib','-march=native', '-DVERSION="%s"' % VERSION_STR],
     'gcc' : ['-O3', '-Izstd/lib','-march=native', '-DVERSION="%s"' % VERSION_STR]}

class build_ext_subclass( build_ext ):
    def build_extensions(self):
        c = self.compiler.compiler_type
        if c in COPT:
           for e in self.extensions:
               e.extra_compile_args = COPT[c]
               print "building with extra", e.extra_compiler_args
        build_ext.build_extensions(self)

setup(
    name='zstd',
    version=VERSION_STR,
    description="ZSTD Bindings for Python",
    author='Sergey Dryabzhinsky, Anton Stuk',
    author_email='sergey.dryabzhinsky@gmail.com',
    url='https://github.com/sigman78/python-zstd',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[
        Extension('zstd', [
            'zstd/lib/fse.c',
            'zstd/lib/zstd.c',
            'src/python-zstd.c'
        ])
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    cmdclass = {'build_ext': build_ext_subclass },
    setup_requires=["nose>=1.0"],
    test_suite = "nose.collector",
)
