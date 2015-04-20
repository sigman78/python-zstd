#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

VERSION = (0, 0, 2)

setup(
    name='zstd',
    version=".".join([str(x) for x in VERSION]),
    description="ZSTD Bindings for Python",
    author='Sergey Dryabzhinsky',
    author_email='sergey.dryabzhinsky@gmail.com',
    url='https://github.com/sergey-dryabzhinsky/python-zstd',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[
        Extension('zstd', [
            'zstd/lib/zstd.c',
            'src/python-zstd.c'
        ], extra_compile_args=[
            "-std=c99",
            "-O2",
            "-Wall",
            "-W",
            "-Wundef",
            "-Izstd/lib",
#           try fortification
#            "-DFORTIFY_SOURCE=2", "-fstack-protector",
#           try hard CPU optimization
#            "-march=native",
#           try Graphite
#            "-floop-interchange", "-floop-block", "-floop-strip-mine", "-ftree-loop-distribution",
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
        'Programming Language :: Python :: 3.4',
    ],
)