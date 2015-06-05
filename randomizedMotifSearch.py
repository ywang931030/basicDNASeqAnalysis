#!/usr/bin/env python
import random
import distance


def profileBuilt(motifs, k, t):
	'''
	motifs is a list of randomly select motifs in each string
	k is the k-mers k argument
	'''
	# initiation the countTable and profile
	# sumCount = []
	# sumCount = [0 for i in range(k)]
	countTable = {}
	countTable['A'] = [1 for i in range(k)]
	countTable['T'] = [1 for i in range(k)]
	countTable['C'] = [1 for i in range(k)]
	countTable['G'] = [1 for i in range(k)]
	profile = {}
	profile['A'] = [0 for i in range(k)]
	profile['C'] = [0 for i in range(k)]
	profile['T'] = [0 for i in range(k)]
	profile['G'] = [0 for i in range(k)]
	# count the presence of bases in each motifs in pattern
	for eachmotif in motifs:
		for i in xrange(k):
			countTable[eachmotif[i]][i] += 1
			# sumCount[i] = sumCount[i] + countTable[eachmotif[i]][i]
	for each in countTable:
		for i in xrange(k):
			profile[each][i] = countTable[each][i] / float(t)
	return profile


def hammingDistance(motifTable, t):
	'''
	Calculate the hamming distance between one motif and others
	motifTable is a list contains t motifs
	The return value will be the score.
	'''
	motif = motifTable[0]
	minDistance = 0
	for i in xrange(t):
		minDistance += distance.hamming(motif, motifTable[i])
	for i in xrange(t):
		motif = motifTable[i]
		dis = 0
		for j in xrange(t):
			dis += distance.hamming(motif, motifTable[j])
		if dis < minDistance:
			minDistance = dis
	return minDistance


def profileMost(profile, Dna, k, t):
	'''
	Find the profilemost motif in each string in Dna
	Dna is a dict contains all k-mers in each string, Dna.keys are the strings, while values are the k-mers
	'''
	profileMostMotifs = []
	for each in Dna:
		profileMost = Dna[each][0]
		maxValue = 1.0
		for i in xrange(k):
			maxValue = maxValue * float(profile[profileMost[i]][i])
		for eachKmers in Dna[each]:
			profileValue = 1.0
			for i in xrange(k):
				profileValue = profileValue * float(profile[eachKmers[i]][i])
			if profileValue > maxValue:
				maxValue = profileValue
				profileMost = eachKmers
		profileMostMotifs.append(profileMost)
	return profileMostMotifs


def randomizedMotifSearch(Dna, k, t, numMotifs):
	'''
	Ramdomized searching for motif
	Dna is a dic contain all k-mers whose keys are the sequences
	k is the argument of k-mers
	t is number of sequences
	numMotifs is the amount of k-mers of each sequences
	'''
	# Generate random number in range(0, numMotifs)
	motifs = []
	for each in Dna:
		id = random.randint(0, numMotifs)
		motifs.append(Dna[each][id])
	bestMotifs = motifs
	bestScore = hammingDistance(bestMotifs, t)
	# Randomized Motif Search, the kernel
	while 1:
		profile = profileBuilt(bestMotifs, k, t)
		motifs = profileMost(profile, Dna, k, t)
		score = hammingDistance(motifs, t)
		if score < bestScore:
			bestMotifs = motifs
			bestScore = score
		else:
			return bestMotifs


def main():
	'''
	randomized search motif
	'''
	k = 15
	t = 20
	seq = {}
	with open('test.txt', 'r') as inputData:
		i = 0
		for line in inputData:
			line = line.strip()
			seq[i] = line
			i += 1
	Dna = {}
	for each in seq:
		Dna[each] = []
		for i in xrange(len(seq[each]) - k + 1):
			Dna[each].append(seq[each][i: i + k])
	# Record the number of motifs in each seq, remeber to minus 1 for it's counting from 0
	numMotifs = len(seq[0]) - k
	# Initialize the bestMotifs and bestScore
	bestMotifs = randomizedMotifSearch(Dna, k, t, numMotifs)
	bestScore = hammingDistance(bestMotifs, t)
	i = 0
	while i <= 200:
		motifs = randomizedMotifSearch(Dna, k, t, numMotifs)
		score = hammingDistance(motifs, t)
		if score < bestScore:
			bestMotifs = motifs
			bestScore = score
		i += 1
	for i in xrange(len(bestMotifs)):
		print bestMotifs[i]
	print bestScore


if __name__ == '__main__':
	main()
