#! /usr/bin/env python3

from setuptools import setup, Extension
from sys import platform

if platform == "win32":
    pymcl_module = Extension("pymcl", sources=["pymcl.c"], include_dirs=["mcl/include"], extra_objects=["mcl/lib/mclbn384_256.lib", "mcl/lib/mcl.lib"])
else:
    pymcl_module = Extension("pymcl", sources=["pymcl.c"], include_dirs=["mcl/include"], extra_objects=["mcl/lib/libmclbn384_256.a", "mcl/lib/libmcl.a"], libraries=["stdc++"])

setup(
    name="pymcl",
    version="1.0",
    description="Python bindings for the mcl library",
    author="Jemtaly",
    author_email="Jemtaly@outlook.com",
    url="https://www.github.com/Jemtaly/pymcl",
    ext_modules=[pymcl_module],
    package_data={"": ["*.pyi", "py.typed"]},
    include_package_data=True,
    zip_safe=False,
)
