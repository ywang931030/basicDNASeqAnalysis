#!/usr/bin/env python
file = open('test.txt', 'r')
Seq = file.read()
freq = {'G': 0, 'C': 0, 'A': 0, 'T': 0, '\n': 0}
for i in Seq:
	freq[i] = freq[i] + 1
GCstat = (float(freq['G']) + freq['C']) / (len(Seq) - freq['\n'])
print GCstat*100