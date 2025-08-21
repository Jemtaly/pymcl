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
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Jemtaly",
    author_email="Jemtaly@outlook.com",
    url="https://www.github.com/Jemtaly/pymcl",
    ext_modules=[pymcl_module],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    extras_require={
        "dev": ["pytest>=6.0.0", "pytest-cov>=2.0.0"],
    },
)
