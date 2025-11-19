#!/usr/bin/env python3

from sys import platform
from setuptools import Extension, setup

if platform == "win32":
    pymcl_module = Extension(
        "pymcl",
        sources=["pymcl.c"],
        include_dirs=["mcl/include"],
        extra_objects=["mcl/lib/mcl.lib"],
    )
else:
    pymcl_module = Extension(
        "pymcl",
        sources=["pymcl.c"],
        include_dirs=["mcl/include"],
        extra_objects=["mcl/lib/libmcl.a"],
        libraries=["stdc++"],
    )

setup(
    name="pymcl",
    version="1.0",
    description="Python bindings for the mcl library",
    author="Jemtaly",
    author_email="Jemtaly@outlook.com",
    url="https://www.github.com/Jemtaly/pymcl",
    ext_modules=[pymcl_module],
    packages=["pymcl"],
    package_data={"pymcl": ["py.typed", "__init__.pyi"]},
    include_package_data=True,
)
