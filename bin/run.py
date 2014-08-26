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
from structs import structs, runners

#parser = argparse.ArgumentParser(description='Make datastructures of kmer overlaps from sets of genes. Save them for loading back in later')
#parser.add_argument("-k", "--kmer_length", type=int, help="length of k to use", default=31)
#parser.add_argument("-f", "--fasta", type=str, help="FASTA sequences to load")
#parser.add_argument("-n", "--sample_sizes", nargs='+', type=int, help="list of number of genes to select")
#parser.add_argument("-i", "--bootstraps", type=int, help="number of bootstrap iterations to select")
#opts = parser.parse_args()

make_reads = False
LARGEST_PARTITION_LIMIT = 0.5 #max proportion of reads allowed in any partition - a parameter for stopping iterative partitioning

def do_a_partition():
	runners.load_graph()
	#runners.partition_graph()
	#runners.merge_partition()
	#runners.annotate_partitions()
	#runners.extract_partitions()
	clean_up()
	
def break_a_lump():
	pass

def count_partition_distributions():
	prog = re.compile('^>(.*)\s+(\d+)\n')
	parts = {}
	seqs = []
	with open(in_file, "r") as f:
		for line in f.readlines():
			m = prog.match(line)
			if m:
				seqs.append(m.group(1))
				if int(m.group(2)) in parts:
					parts[int(m.group(2))].append(m.group(1))
				else:
					parts[int(m.group(2))] = [m.group(1)]
				return max(parts.keys()), list(set(seqs)), parts

def clean_up():
	pass

def break_lump(lump):
	#runners.load_graph()
	#runners.make_initial_stop_tags()
	
	#runners.partition_graphs()
	#runners.filter_stoptags()

def assemble():
	pass

def break_lumps(lump_list):
	for lump in lump_list:
		break_lump(lump)
		do_a_partition()
		count_partition_distributions()

def main():
	if make_reads:
		runners.make_reads()
	##check state of assembly prior
	runners.velvet()
	#runners.summarise_assembly()
	##count kmers prior
	#runners.load_into_counting(k=31,n=4, b=2e8, t=1, outfile='meh', infile="../data/3_rgenes.fna", )
	#runners.abundance_dist()
	##normalize
	#runners.normalize_by_median()
	##count normalised kmers
	#runners.load_into_counting()
	#runners.abundance_dist()
	
	
	#largest_partition = 1.0 
	#do_a_partition()
	#largest_partition = count_partition_distributions()
	##remove knots iteratively
	#while LARGEST_PARTITION_LIMIT < largest_partition:
		#break_lumps()


if __name__ == "__main__":
	main()