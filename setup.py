#!/usr/bin/env python3

from tempfile import TemporaryDirectory
from pathlib import Path
from urllib.request import urlopen
import tarfile
import shutil

import os
import subprocess
import sys
from setuptools import setup
from setuptools.command.sdist import sdist
from setuptools.command.build_ext import build_ext

from pybind11.setup_helpers import Pybind11Extension


IS_WINDOWS = sys.platform == "win32"

MCL_TAG = "v3.04"
MCL_URL = f"https://github.com/herumi/mcl/archive/refs/tags/{MCL_TAG}.tar.gz"

ROOT = Path(__file__).parent.resolve()
THIRD_PARTY_DIR = ROOT / "third_party"
MCL_DIR = THIRD_PARTY_DIR / "mcl"
MCL_VERSION_MARKER = MCL_DIR / f".mcl_version_{MCL_TAG}"
MCL_INCLUDE_DIR = MCL_DIR / "include"
MCL_LIBRARY_DIR = MCL_DIR / "lib"
MCL_LIB = MCL_LIBRARY_DIR / ("mcl.lib" if IS_WINDOWS else "libmcl.a")


def fetch_mcl():
    if MCL_VERSION_MARKER.exists():
        print("Using cached mcl library.")
        return

    if MCL_DIR.exists():
        shutil.rmtree(MCL_DIR)

    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        download_path = temp_path / "mcl.tar.gz"
        extract_path = temp_path / "extracted"

        print("Downloading mcl library...")
        with urlopen(MCL_URL) as response, open(download_path, "wb") as out_file:
            shutil.copyfileobj(response, out_file)

        print("Extracting mcl library...")
        with tarfile.open(download_path, "r:gz") as tar:
            tar.extractall(path=extract_path)

        source_root = next(extract_path.iterdir())
        MCL_DIR.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(source_root, MCL_DIR)

    MCL_VERSION_MARKER.touch()


def build_mcl():
    fetch_mcl()

    if MCL_LIB.exists():
        print("Using existing built mcl library.")
        return

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


class CustomSdist(sdist):
    def run(self):
        fetch_mcl()
        super().run()


class CustomBuildExt(build_ext):
    def run(self):
        build_mcl()
        super().run()


module = Pybind11Extension(
    "pymcl._pymcl",
    sources=["src/pymcl/_pymcl.cpp"],
    include_dirs=[str(MCL_INCLUDE_DIR)],
    extra_objects=[str(MCL_LIB)],
)
module.cxx_std = 17  # Require C++17 standard


setup(
    ext_modules=[module],
    cmdclass={
        "sdist": CustomSdist,
        "build_ext": CustomBuildExt,
    },
    package_dir={"": "src"},
    packages=["pymcl"],
    package_data={"pymcl": ["_pymcl.pyi", "py.typed"]},
    include_package_data=True,
)
