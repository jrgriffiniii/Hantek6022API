#!/usr/bin/env python

import os, sys

root_path = os.getcwd()
py_ht6022_path = os.path.join(root_path, "PyHT6022")
sys.path.append(py_ht6022_path)

import PyHT6022
