#!/usr/bin/env python
# encoding: utf-8
"""
run.py

Created by Dan MacLean (TSL) on 2014-05-21.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

import sys
import time
import random
import argparse
from Bio import SeqIO
from subprocess import call
import runners

#parser = argparse.ArgumentParser(description='Make datastructures of kmer overlaps from sets of genes. Save them for loading back in later')
#parser.add_argument("-k", "--kmer_length", type=int, help="length of k to use", default=31)
#parser.add_argument("-f", "--fasta", type=str, help="FASTA sequences to load")
#parser.add_argument("-n", "--sample_sizes", nargs='+', type=int, help="list of number of genes to select")
#parser.add_argument("-i", "--bootstraps", type=int, help="number of bootstrap iterations to select")
#opts = parser.parse_args()


def main():
	runners.load_into_counting(prog='load_into_counting', k=31,n=4, b=2e8, t=1, outfile='meh', infile="../data/3_rgenes.fna", )
	


if __name__ == "__main__":
	main()