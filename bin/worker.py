#!/usr/bin/env python
# encoding: utf-8
"""
worker.py

Created by Dan MacLean (TSL) on 2014-05-28.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

import sys
import os
import structs
import time
import pickle


def main():
	start = time.clock()
	kmer_info = structs.KmerInfo(sys.argv[1],sys.argv[2])
	elapsed = (time.clock() - start)
	print >> sys.stderr, "built datastruct in ", elapsed
	filename = "_".join(['pickled', sys.argv[1]])
	try:
		pickle.dump( kmer_info, open( filename, "wb" ) )
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit


if __name__ == '__main__':
	main()

