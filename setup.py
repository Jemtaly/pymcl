#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path
from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext

IS_WINDOWS = sys.platform == "win32"

ROOT = Path(__file__).parent.resolve()
CACHE_DIR = ROOT / ".cache"
MCL_DIR = CACHE_DIR / "mcl"
MCL_INCLUDE_DIR = MCL_DIR / "include"
MCL_LIBRARY_DIR = MCL_DIR / "lib"
MCL_LIB = MCL_LIBRARY_DIR / ("mcl.lib" if IS_WINDOWS else "libmcl.a")


class CustomBuildExt(build_ext):
    """Custom build_ext command to build the mcl library before building the extension."""

    def run(self):
        self.build_mcl()
        super().run()

    def build_mcl(self):
        if not MCL_DIR.exists():
            print("Cloning mcl repository...")
            subprocess.check_call(["git", "clone", "https://github.com/herumi/mcl", str(MCL_DIR)])

        if not MCL_LIB.exists():
            print("Building mcl library...")
            if IS_WINDOWS:
                subprocess.check_call(
                    ["mklib.bat"],
                    cwd=MCL_DIR,
                    shell=True,
                    env=os.environ | {"CL": "/MD"},
                )
            else:
                subprocess.check_call(
                    ["make", "-j4"],
                    cwd=MCL_DIR,
                )


module = Pybind11Extension(
    "pymcl._pymcl",
    sources=["src/pymcl/_pymcl.cpp"],
    include_dirs=[str(MCL_INCLUDE_DIR)],
    extra_objects=[str(MCL_LIB)],
)


setup(
    ext_modules=[module],
    cmdclass={"build_ext": CustomBuildExt},
    package_dir={"": "src"},
    packages=["pymcl"],
    package_data={"pymcl": ["_pymcl.pyi", "py.typed"]},
    include_package_data=True,
)
