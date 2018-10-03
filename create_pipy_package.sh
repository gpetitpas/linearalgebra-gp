#!/usr/bin/env bash

# install dependencies
pip install -r requirements.txt

# Create pip package
python3.6 setup.py install
