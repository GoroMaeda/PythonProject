# -*- coding: utf-8 -*-
"""Resize image file module.

Keyword arguments:
args[1] -- Image file path
args[2] -- Image file resize magnification
"""
import os
import sys
from PIL import Image

# Get program arguments
args = sys.argv
argc = len(args)

print("argc=[" + str(argc) + "]")
print(args)

# Program arguments check
if (argc != 2):
    print("usage: python " + os.path.basename(args[0]) + " arg1")
    quit()

# Open image file
img = Image.open(args[1])
print("---- Base file infomation ----")
print("  File type  : %s" %img.format)
print("  File width : %d" %img.size[0])
print("  File height: %d" %img.size[1])
print("  File mode  : %s" %img.mode)
print("------------------------------")

# Resize image file
width  = int(img.size[0] * 0.4)
height = int(img.size[1] * 0.4)
imgResize = img.resize( (width, height) )
imgResize.save('D:\\img\\resize.jpg', quality=100, optimize=True)

print("--- Resize file infomation ---")
print("  File type  : %s" %imgResize.format)
print("  File width : %d" %imgResize.size[0])
print("  File height: %d" %imgResize.size[1])
print("  File mode  : %s" %imgResize.mode)
print("------------------------------")
