#!/usr/bin/env python3

from logging import error
from pprint import pprint
from re import compile, IGNORECASE

vowels = 'aeiouáéíóúàèìòùäëïöüâêîôûå'
emphasized = 'áéíóú'
filter_single = compile('[^{0}]*[{0}][^{0}]*'.format(emphasized), IGNORECASE)#FIXME
filter_double = compile('[{0}]{{2}}[^{0}]*'.format(emphasized), IGNORECASE)
filter_triple = compile('[{}]{{2}}[{}]'.format(emphasized, vowels), IGNORECASE)
single_lower = []
single = []
double_lower = []
double = []
triple_lower = []
triple = []

with open('words.tsv', 'r') as words:
    for line in words:
        word, category = line.strip().split('\t')
        if category == '0':
            continue
        iterator = filter_single.findall(word)
        first = True
        for match in iterator:
            if first:
                if word.islower():
                    single_lower.append(word)
                else:
                    single.append(word)
                first = False
            else:
                error('Multiple matches found when searching single in {}'.format(word))
        iterator = filter_double.finditer(word)
        first = True
        for match in iterator:
            if first:
                if word.islower():
                    double_lower.append(word)
                else:
                    double.append(word)
                first = False
            else:
                error('Multiple matches found when searching double in {}'.format(word))
        iterator = filter_triple.finditer(word)
        first = True
        for match in iterator:
            if first:
                if word.islower():
                    triple_lower.append(word)
                else:
                    triple.append(word)
                first = False
            else:
                error('Multiple matches found when searching triple in {}'.format(word))

print('Emphasized words containing upper case characters:')
for word in sorted(single):
    if word.lower() not in single_lower:
        print(word)
for word in sorted(double):
    if word.lower() not in double_lower:
        print(word)
for word in sorted(triple):
    if word.lower() not in triple_lower:
        print(word)

print('Emphasized words with only lower case characters:')
for word in sorted(single_lower):
    print(word)
for word in sorted(double_lower):
    print(word)
for word in sorted(triple_lower):
    print(word)
