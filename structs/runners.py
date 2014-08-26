#!/usr/bin/env python
# encoding: utf-8
"""
runners.py

Created by Dan MacLean (TSL) on 2014-08-19.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

import sys
import os
import subprocess
import unittest
import logging
import time

binaries = {

"load_into_counting" : "../bin/khmer_local/khmer/scripts/load-into-counting.py",
"abundance_dist" : "../bin/khmer_local/khmer/scripts/abundance-dist.py",
"normalize_by_median" : "../bin/khmer_local/khmer/scripts/normalize-by-median.py",
"do_partition" : "../bin/khmer_local/scripts/do-partition.py",
"load_graph" : "../bin/khmer_local/khmer/scripts/load-graph.py",
"stop_tags" : "../bin/khmer_local/khmer/scripts/make-initial-stoptags.py",
"partition_graph" : "../bin/khmer_local/khmer/scripts/partition-graph.py",
"find_knots" : "../bin/khmer_local/khmer/scripts/find-knots.py",
"filter_stoptags" : "../bin/khmer_local/khmer/scripts/filter-stoptags.py",
"extract_partitions" : "../bin/khmer_local/khmer/scripts/extract-partitions.py",

}


logging.basicConfig(filename='runs.log',level=logging.DEBUG)
scratch = 'scratch/'	

def make_reads(**kwargs):
	command = kwargs["binary"] 
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

def get_time():
	return time.strftime("%H:%M:%S | %d/%m/%Y")

def load_into_counting(**kwargs):
	"""runs the khmer load into counting script"""
	outfile = scratch + kwargs["outfile"]
	command = "python {0} --ksize {1} --n_tables {2} --min-tablesize {3} --threads {4} {5} {6}".format(binaries["load_into_counting"], kwargs["k"], kwargs["n"], kwargs["b"], kwargs["t"], outfile, kwargs["infile"] )
	run_generic(command)

def run_load_graph(**kwargs):
	a = kwargs
	command = "python {0} --ksize {1} --n_tables {2} --min-tablesize {3} {4} {5}".format(binaries["load_graph"], a["k"], a["n"], a["min_tbl_size"], a["basename"], a["input_file"])
	run_generic_script(command)


def run_generic(command):
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	o,e = str(out), str(err)
	if e:
		e = e.replace("\n", "<slashn>")
		time = get_time()
		logging.warning("FAILED\t{0}\t{1}\t{2}".format(command, e, time) )
	if o:
		o = o.replace("\n","<slashn>")
		logging.warning("DONE\t{0}\t{1}\t{2}".format(command, e, time) )
