#!/bin/bash
echo "Installing pymcl..." &&
sudo apt update &&
sudo apt-get install -y libgmp-dev &&
git clone https://github.com/herumi/mcl &&
cd mcl &&
make -j4 &&
cd .. &&
sudo pip3 install . &&
echo "pymcl installed successfully!"
