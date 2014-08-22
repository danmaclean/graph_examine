#!/usr/bin/env python
# encoding: utf-8
"""
profile.py

Created by Dan MacLean (TSL) on 2014-05-23.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

import os

def main():
	os.system("python -m cProfile -s 'time' run.py 3_rgenes.fna")


if __name__ == '__main__':
	main()

