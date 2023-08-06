#!/bin/bash

# This script expects to be in the pytorch root folder
if [[ ! -f 'run_tests.sh' ]]; then
    echo "run_tests.sh expects to be run from test directory (Adifpy/test) " \
         "but I'm actually in $(pwd)"
    exit 2
fi

# Go to the root directory
cd ../..

# Install dependencies and the package
python3 -m pip install pytest pytest-cov numpy matplotlib .

# Run pytest coverage
python3 -m pytest --cov-report term --cov=Adifpy
