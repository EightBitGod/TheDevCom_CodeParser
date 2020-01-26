#!/usr/bin/python

import argparse
import ply.lex as lex
import ply.yacc as yacc

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
print('Output : {}\n'.format(args.output))

# Open input file and read the contents into a string
try:
    input_file = open(args.input,'r')
except Exception as e:
    print('{}\nExiting...'.format(e))
    exit(1)

# Program stored as string
input_program = input_file.read()

print(input_program)

# Close the file object
input_file.close()

# Add all the possible tokens in C language inside this multiline comment so that we don't leave anything!
'''
    number, +, -, /, *
'''

# Add all the valid tokens in this list

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
)

# Regular expression rules for tokens format: t_<TOKEN>, Use the format as specified below. Check for special characters.
# Simple tokens

t_NUMBER = r'd'
t_PLUS    = r'\+'
t_MINUS   = r'-'

# Complex tokens

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# TODO Add parser code here

