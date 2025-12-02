#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path
from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext

IS_WINDOWS = sys.platform == "win32"

ROOT = Path(__file__).parent.resolve()
VENDOR_DIR = ROOT / "vendor"
MCL_DIR = VENDOR_DIR / "mcl"


class CustomBuildExt(build_ext):
    """Custom build_ext command to build the mcl library before building the extension."""

    def run(self):
        self.build_mcl()
        super().run()

    def build_mcl(self):
        if not MCL_DIR.exists():
            print("Cloning mcl repository...")
            subprocess.check_call(["git", "clone", "https://github.com/herumi/mcl", str(MCL_DIR)])

        print("Building mcl library...")
        if IS_WINDOWS:
            subprocess.check_call(["mklib.bat"], cwd=MCL_DIR, shell=True)
        else:
            subprocess.check_call(["make", "-j4"], cwd=MCL_DIR)


MCL_INCLUDE_DIR = MCL_DIR / "include"
MCL_LIBRARY_DIR = MCL_DIR / "lib"
MCL_LIB = MCL_LIBRARY_DIR / ("mcl.lib" if IS_WINDOWS else "libmcl.a")

module = Pybind11Extension(
    "pymcl._pymcl",
    sources=["src/pymcl/_pymcl.cpp"],
    include_dirs=[str(MCL_INCLUDE_DIR)],
    extra_objects=[str(MCL_LIB)],
)

ext_modules = [module]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": CustomBuildExt},
    packages=["pymcl"],
    package_data={"pymcl": ["_pymcl.pyi", "py.typed"]},
    include_package_data=True,
)
