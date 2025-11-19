#!/usr/bin/env python3
"""Setup script for pymcl - build configuration for C extension module."""

from setuptools import setup, Extension
from sys import platform

# Configure the C extension module based on platform
if platform == "win32":
    pymcl_module = Extension(
        "pymcl",
        sources=["pymcl.c"],
        include_dirs=["mcl/include"],
        extra_objects=["mcl/lib/mclbn384_256.lib", "mcl/lib/mcl.lib"]
    )
else:
    pymcl_module = Extension(
        "pymcl",
        sources=["pymcl.c"],
        include_dirs=["mcl/include"],
        extra_objects=["mcl/lib/libmclbn384_256.a", "mcl/lib/libmcl.a"],
        libraries=["stdc++"]
    )

# Setup with extension module
# Project metadata is now defined in pyproject.toml
setup(
    ext_modules=[pymcl_module],
    package_data={"": ["*.pyi"]},
    include_package_data=True,
)
