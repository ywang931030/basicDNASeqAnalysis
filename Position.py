#!/usr/bin/env python
## input a string and a pattern
## output the position of the pattern in the string
## notice that python is counting from 0

file = open('test.txt', 'r')
DNAString = file.read()
Pattern = raw_input('Pattern:')
## original
#i = 0
#k = len(Pattern)
#while i <= len(DNAString):
#	if DNAString[i: i + k: 1] == Pattern:
#		print i + 1
#	i += 1
## more pythonic
print ' '.join([str(i + 1) for i in xrange(len(DNAString)) if DNAString[i : i + len(Pattern)] == Pattern])