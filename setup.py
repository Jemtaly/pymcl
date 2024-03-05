#! /usr/bin/env python3

from setuptools import setup, Extension

pymcl_module = Extension("pymcl", sources=["pymcl.c"], include_dirs=["mcl/include"], extra_objects=["mcl/lib/libmclbn384_256.a", "mcl/lib/libmcl.a"], libraries=["stdc++"])

setup(
    name="pymcl",
    version="1.0",
    description="Python bindings for the MCL library",
    author="Jemtaly",
    author_email="Jemtaly@outlook.com",
    url="https://www.github.com/Jemtaly/pymcl",
    ext_modules=[pymcl_module],
)
