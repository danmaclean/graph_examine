#!/usr/bin/env python
# encoding: utf-8
"""
structs_test.py

Created by Dan MacLean (TSL) on 2014-08-14.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""
import unittest
import structs
import traceback
import os

class structsTests(unittest.TestCase):


	def setUp(self):
		fasta = ">test_1\nATGCTGGG\n"
		try:
			f = open("test.fa", "w")
			f.write(fasta)
			f.close()
			return True
		except:
			print "couldnot setup"
		
	def tearDown(self):
		try:
			os.remove("test.fa")
		except Exception as e:
			print "Error removing file 'test.fa' after test: {0}\n {1}".format(e, traceback.format_exc() )

	
	def test_get_kmers(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		kmers = kmer_info.kmer_attrs.keys()
		self.assertEqual(len(kmers), 4)
		self.assertEqual(sorted(kmers),sorted(['atgctgg', 'tgctggg', 'ccagcat', 'cccagca']) )
	
	def test_add_kmers(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		self.assertEqual(kmer_info['atgctgg']['coverage'], 1)
		kmer_info.add_kmer('atgctgg', 'test_1')
		self.assertEqual(kmer_info['atgctgg']['coverage'], 2)
		self.assertEqual(kmer_info['atgctgg']['origin'].keys(), ['test_1'])
		
	def test_chop_left(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		self.assertEqual(kmer_info.chop_left('daniel'), 'aniel')
	
	def test_chop_right(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		self.assertEqual(kmer_info.chop_right('daniel'), 'danie')
	
	def test_get_matches(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		expected_matches_at = [0]
		got_matches_at = kmer_info.get_matches(['aniel'],['aniel', 'trevor'])
		self.assertEqual( got_matches_at, expected_matches_at )
	
	def test_get_edges(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		expected_edges = [('atgctgg', 'tgctggg'), ('cccagca', 'ccagcat')]
		self.assertEqual(sorted(kmer_info.edges), sorted(expected_edges))
	
	def test_make_igraph(self):
		kmer_info = structs.KmerInfo('test.fa',7)
		g = kmer_info.igraph
		expected_origins = ['test_1']
		expected_coverage = [1,1,1,1]
		expected_origin = [ ['test_1'], ['test_1'], ['test_1'], ['test_1']]
		self.assertEqual(g["origins"], expected_origins)
		self.assertEqual(g.vs["origin"], expected_origin)
		self.assertEqual(g.vs["coverage"], expected_coverage)

