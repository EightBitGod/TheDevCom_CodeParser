#!/usr/bin/python

import argparse

# Create a parser to take filenames as command line arguments
parser = argparse.ArgumentParser(description='Code Parser input arguments')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
args = parser.parse_args()

'''
	Usage : 
	Input File : args.input
	Output File : args.output
'''
# Test - Remove these
print('Input : {}'.format(args.input))
print('Output : {}'.format(args.output))

# TODO Add parser code here
