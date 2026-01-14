#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path
from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext

IS_WINDOWS = sys.platform == "win32"

MCL_GIT_URL = "https://github.com/herumi/mcl"
MCL_GIT_REF = "v3.04"

ROOT = Path(__file__).parent.resolve()
CACHE_DIR = ROOT / ".cache"
MCL_DIR = CACHE_DIR / "mcl"
MCL_INCLUDE_DIR = MCL_DIR / "include"
MCL_LIBRARY_DIR = MCL_DIR / "lib"
MCL_LIB = MCL_LIBRARY_DIR / ("mcl.lib" if IS_WINDOWS else "libmcl.a")
MCL_BUILD_REF_MARKER = MCL_LIBRARY_DIR / ".build_ref"


class CustomBuildExt(build_ext):
    """Custom build_ext command to build the mcl library before building the extension."""

    def run(self):
        self.build_mcl()
        super().run()

    def build_mcl(self):
        if (
            MCL_LIB.exists()
            and MCL_BUILD_REF_MARKER.exists()
            and MCL_BUILD_REF_MARKER.read_text().strip() == MCL_GIT_REF
        ):
            print("mcl library is up to date. Skipping build.")
            return

        print("Preparing to build mcl library...")
        if not MCL_DIR.exists():
            subprocess.check_call(["git", "clone", MCL_GIT_URL, str(MCL_DIR)])
        else:
            subprocess.check_call(["git", "fetch", "--all"], cwd=MCL_DIR)
        subprocess.check_call(["git", "checkout", MCL_GIT_REF], cwd=MCL_DIR)

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

        print("mcl library built successfully.")
        MCL_BUILD_REF_MARKER.write_text(MCL_GIT_REF)


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
