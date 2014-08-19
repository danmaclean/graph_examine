# Notes

## To run on HPC.
The script `run.py` is the master. It will divide up the fasta file into bits and run `worker.py` with each subfile.

From the submission node:

> python run.py -k 31 -f <fasta_file> -i <bootstrap repetitions>  -n [number of genes to choose]
	
eg 

> python run.py -k 31 -f my_genes.fa -i 10 -n 2 5 10

You will end up with 2 sets of files, the sampled fasta and the pickled data structures. Filenames will be as:

> number_of_genes _ bootstrap_iteration _ fasta_file
> pickled _ number_of_genes _ bootstrap_iteration _ fasta_file


**This script does not clean up after itself**



