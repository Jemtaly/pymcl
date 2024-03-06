@echo off
echo Installing pymcl...
git clone https://github.com/herumi/mcl
cd mcl
call mklib.bat
cd ..
pip install .
echo pymcl installed successfully!
