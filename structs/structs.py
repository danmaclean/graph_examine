#!/usr/bin/env python
# encoding: utf-8
"""
structs.py

Created by Dan MacLean (TSL) on 2014-05-21.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

import sys
import os
import unittest
import itertools
from time import sleep
from Bio import SeqIO
import igraph

class KmerInfo:
	def __init__(self,fasta,k=31):
		self.edges = []
		self.kmer_attrs = {}
		self.make_kmer_graph(fasta,int(k))
		self.igraph = KmerInfo.make_igraph(self)
	
	def __getitem__(self,key):
		return self.kmer_attrs[key]
	
	def make_kmer_graph(self,fasta,k):
		self.get_kmers(fasta,k)
		self.get_edges()
	
	def add_kmer(self,kmer,seq_of_origin):
		kmer = str(kmer.lower())
		if str(kmer) in self.kmer_attrs:
			self.kmer_attrs[str(kmer)]['coverage'] = self.kmer_attrs[str(kmer)]['coverage'] + 1
			self.kmer_attrs[str(kmer)]['origin'][seq_of_origin] = 1
		else:
			self.kmer_attrs[str(kmer)] = {'coverage':1, 'origin':{seq_of_origin:1} }
	
	def get_kmers(self,fasta,k=31):
		for s in SeqIO.parse(fasta, "fasta"):
			fwd = str(s.seq)
			rev = str(s.reverse_complement().seq)
			for i in range(len(fwd) - k + 1):
				self.add_kmer(fwd[i:i+k],s.id)
				self.add_kmer(rev[i:i+k],s.id)
	
	def get_edges(self,chunk_size=3):
		kmer_list = self.kmer_attrs.keys()
		chopped_left = [self.chop_left(i) for i in kmer_list]
		chopped_right = [self.chop_right(i) for i in kmer_list]
		for i in range(len(chopped_left)): 
			match_indices = self.get_matches([chopped_left[i]],chopped_right)
			matches = [ (kmer_list[i], kmer_list[j]) for j in match_indices if i != j]
			self.edges.extend(matches)
		
	def get_matches(self, a, b):
		reverse_map = {x:i for i, x in enumerate(a)}
		return [ i for i, x in enumerate(b) if x in reverse_map]
	
	def chop_left(self,kmer):
		return kmer[1:]
	
	def chop_right(self,kmer):
		return kmer[:-1]
	
	def make_igraph(self):
		'''makes an igraph from a kmer overlap object'''
		g = igraph.Graph(directed=True)
		kmers = self.kmer_attrs.keys()
		id_map = {kmers[i] : i for i in range(len(kmers)) }
		g.add_vertices(len(kmers))
		g.vs["origin"] = KmerInfo.origin_list(self, kmers)
		g.vs["coverage"] = KmerInfo.get_coverage(self, kmers)
		g["origins"] = KmerInfo.unique_origin_list(self,kmers)
		g.add_edges([(id_map[i[0]],id_map[i[1]]) for i in self.edges ])
		return g
	
	def origin_list(self, kmers):
		'''returns list of sequence origins for all vertices'''
		return [self.kmer_attrs[str(kmer)]['origin'].keys() for kmer in kmers]

	def unique_origin_list(self, kmers):
		'''returns list of unique origin names'''
		l = KmerInfo.origin_list(self,kmers)
		return list(set(itertools.chain(*l)))

	def get_coverage(self, kmers):
		return [self.kmer_attrs[str(kmer)]['coverage'] for kmer in kmers]