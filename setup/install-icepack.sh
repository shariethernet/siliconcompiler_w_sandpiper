#!/bin/sh

set -e

sudo apt-get install -y build-essential clang bison flex libreadline-dev \
                        gawk tcl-dev libffi-dev git mercurial graphviz   \
                        xdot pkg-config python python3 libftdi-dev \
                        qt5-default python3-dev libboost-all-dev cmake libeigen3-dev

mkdir -p deps
cd deps

git clone https://github.com/YosysHQ/icestorm.git icestorm
cd icestorm
make -j$(nproc)
sudo make install
cd -