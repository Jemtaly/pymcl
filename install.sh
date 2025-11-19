#!/usr/bin/bash

echo "Installing pymcl..." &&
sudo apt update &&
sudo apt-get install -y libgmp-dev &&
rm -rf mcl &&
git clone https://github.com/herumi/mcl &&
cd mcl &&
make -j4 &&
cd .. &&
python3 -m pip install . &&
echo "pymcl installed successfully!"
