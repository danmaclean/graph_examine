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

parser = argparse.ArgumentParser(description='Make datastructures of kmer overlaps from sets of genes. Save them for loading back in later')
parser.add_argument("-k", "--kmer_length", type=int, help="length of k to use", default=31)
parser.add_argument("-f", "--fasta", type=str, help="FASTA sequences to load")
parser.add_argument("-n", "--sample_sizes", nargs='+', type=int, help="list of number of genes to select")
parser.add_argument("-i", "--bootstraps", type=int, help="number of bootstrap iterations to select")
opts = parser.parse_args()

def make_graph(kmer_info):
	g = nx.Graph()
	for i in kmer_info.kmer_attrs:
		g.add_node(i, kmer_info[i])
	g.add_edges_from(kmer_info.edges)
	return g

def select_from_fasta(fasta, sample_size, iteration):
	seq_list = list(SeqIO.parse(fasta, "fasta"))
	filename = "_".join([str(sample_size), str(iteration),fasta ] ) 
	indices = random.sample(range(len(seq_list)), sample_size)
	try:
	 	write_fasta( [seq_list[i] for i in indices], filename )
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit
	return filename


def write_fasta(seq_list, filename):
	output_handle = open(filename, "w")
	count = SeqIO.write(seq_list, output_handle, "fasta")
	output_handle.close()
	return True

def run_job(fasta,kmer_length):
	print "running job with file {0} and k {1}".format(fasta,kmer_length)
	call(["bsub", "-q TSL-Test128", "python", "worker.py", fasta, str(kmer_length)])

def main(opts):
	for sample_size in opts.sample_sizes:
		mini_fasta_file_names = [select_from_fasta(opts.fasta,sample_size, i) for i in range(opts.bootstraps) ]
		for fasta in mini_fasta_file_names:
			run_job(fasta,opts.kmer_length)



if __name__ == "__main__":
	main(opts)
