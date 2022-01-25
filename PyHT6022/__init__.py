__author__ = 'Robert Cope'

import os, sys

root_path = os.getcwd()
lib_usb_scope_path = os.path.join(root_path, "PyHT6022", "LibUsbScope")
sys.path.append(lib_usb_scope_path)

import PyHT6022.LibUsbScope

firmware_path = os.path.join(root_path, "PyHT6022", "Firmware")
sys.path.append(firmware_path)

import PyHT6022.Firmware

