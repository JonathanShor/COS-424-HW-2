'''
Created on Mar 23, 2015

@author: jonathanshor
'''
import numpy as np
import sys
from optparse import OptionParser

TRAIN_FNAME = "intersected_final_chr1_cutoff_20_train_revised.bed"
SAMPLE_FNAME = "intersected_final_chr1_cutoff_20_sample.bed"
TEST_FNAME = "intersected_final_chr1_cutoff_20_test.bed"

def read_bed_dat_sample(myfile):
	return np.loadtxt(myfile, dtype=[('Chrom', np.str_, 4), ('Start', np.int32), ('End', np.int32), ('Strand', np.str_, 1), ('Beta', np.float32), ('450k', np.int32)])

def read_bed_dat_train(myfile):
	return np.loadtxt(myfile, dtype=[('Chrom', np.str_, 4), ('Start', np.int32), ('End', np.int32), ('Strand', np.str_, 1), ('Beta', np.float32, (33)), ('450k', np.int32)])

def main(argv):
	parser = OptionParser()
	parser.add_option("-p", "--path", dest="path", help='read bed data fom PATH', metavar='PATH')
	(options, args) = parser.parse_args()     
	path = options.path
	print "PATH = " + path
	train = read_bed_dat_train(path + TRAIN_FNAME)
	sample = read_bed_dat_sample(path + SAMPLE_FNAME)
    
	print "sample[0] = %s" % sample[0]
	print "train[0] = %s" % train[0]
	print "len(train) = %s" % len(train)
	print "train['Beta'][0] = %s" % train['Beta'][0]

if __name__ == '__main__':
    main(sys.argv[1:])
