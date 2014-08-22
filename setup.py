#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Created by Dan MacLean (TSL) on 2014-08-15.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

from setuptools import setup

setup(name='graph_examine',
      version='0.0.0',
      description='some very structures for kmer graphs',
      url='http://github.com/danmaclean',
      author='Dan MacLean',
      author_email='maclean.daniel@gmail.com',
      license='GPL3',
      packages=['structs','structs.test'],
      zip_safe=False)