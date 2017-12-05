#!/usr/bin/env python3

from logging import warn, error
from os import path
from pprint import pprint
from re import compile, IGNORECASE

destination = 'words.tsv'
if path.isfile(destination):
    warn('Omitting analysis as file {} already exists. Please, review or process it.'.format(destination))
    infile = open(destination, 'r')
    line_number = 0
    missing = 0
    first = 0
    last = 0
    for line in infile:
        line_number += 1
        line = line[:-1]
#        print(line)
        if line[-1] == '\t':
            missing += 1
            if first == 0:
                first = line_number
            last = line_number
        split = line.split('\t')
        if len(split) == 0:
            error('Fix missing tabs in {} for line {} with word {}'.format(destination, line_number, split[0]))
        elif len(split) > 2:
            error('Fix excessive tabs in {} for line {} with word {}'.format(destination, line_number, split[0]))
        if '\t ' in line or ' \t' in line or '  ' in line:
            error('Fix excessive whitespace in {} for line {} with word {}'.format(destination, line_number, split[0]))
    if missing:
        error('Add {} missing classifications to file {}, starting at line {} and ending at line {}'.format(missing, destination, first, last))
    exit(0)

filter = compile('.*[áéíóú].*', IGNORECASE)
infile = open('alle-goed.txt', 'r')
outfile = open(destination, 'w')

for line in infile:
    word = line.strip()
    if filter.match(word):
        outfile.write('{}\t\n'.format(word))
        
        #TODO geaccentueerde namen uitsluiten