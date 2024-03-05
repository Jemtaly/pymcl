#!/bin/bash
echo "Installing pymcl..." &&
sudo apt update &&
sudo apt-get install -y libgmp-dev && 
sudo apt-get install -y libomp-dev &&
git clone https://github.com/herumi/mcl &&
cd mcl &&
make -j4 &&
cd .. &&
sudo pip3 install . &&
echo "pymcl installed successfully!"
