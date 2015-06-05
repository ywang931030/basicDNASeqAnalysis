#!/usr/bin/env python
Index = {}
with open('test.txt') as file:
	for line in file:
		line = line.strip()
## Build Index for countstatis
#read from file so that if line begins with >, store as key and all following as value for that key
		if line[0] == '>':
			Index[line.strip('>')] = ""
			temp = line.strip('>')
		else:
			Index[temp] += line
print Index
## Build Consensus Matrix Index
k = len(Index['Rosalind_4820'])
ConIndex = {'A': [0] * k,'T': [0] * k, 'G': [0] * k, 'C': [0] * k}
j = 1
for j in xrange(k):
	for i in Index:
		ConIndex[Index[i][j - 1]][j - 1] = ConIndex[Index[i][j - 1]][j - 1] + 1
print ConIndex
ConString = ''
for i in xrange(k):
	Consensus = max(ConIndex['A'][i], ConIndex['T'][i],ConIndex['C'][i],ConIndex['G'][i])
	for j in ConIndex:
		if Consensus == ConIndex[j][i]:
		ConString += j
	print ConString
