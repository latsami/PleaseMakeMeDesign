#! /usr/bin/env python -u

file = open('stop_english', 'r')
stopwords = file.readlines()
file.close()


import sys
lexique = sys.stdin.read()
lexique = lexique.decode('utf-8').split('\n')

keywords = ''

for ligne in lexique:
    if ligne not in stopwords:
        keywords+= ligne + '\n'

print keywords.encode('utf-8')