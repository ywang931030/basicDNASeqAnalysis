#!/usr/bin/env python
import distance


SUM = []


def profileBuilt(pattern, k, profile, countTable):
	'''
	Build the profile
	First form a count table
	Then form the profile by calculate the presence rate of each bases in every position
	Notice:
	pattern is a string, not a list
	count is the count table

	'''
	global SUM
	for i in xrange(k):
		countTable[pattern[i]][i] += 1
		SUM[i] = SUM[i] + countTable[pattern[i]][i]
	for each in countTable:
		for i in xrange(k):
			profile[each][i] = countTable[each][i] / float(SUM[i])
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


def profileMost(pattern, profile, k):
	'''
	Calculate the kmers in pattern of most profile according to the profile matrix
	'''
	allKmers = {}
	for i in xrange(len(pattern) - k + 1):
		allKmers[pattern[i: i + k]] = pattern[i: i + k]
	maxValue = 1.0
	profileMost = pattern[0: k]
	for i in xrange(k):
		maxValue = maxValue * float(profile[profileMost[i]][i])
	for each in allKmers:
		profileValue = 1.0
		for i in xrange(len(allKmers[each])):
			profileValue = profileValue * float(profile[allKmers[each][i]][i])
		allKmers[each] = profileValue
		if profileValue > maxValue:
			maxValue = profileValue
			profileMost = each
	return profileMost


def main():
	k = 15
	t = 20
	profile = {}
	profile['A'] = [0 for i in range(k)]
	profile['C'] = [0 for i in range(k)]
	profile['T'] = [0 for i in range(k)]
	profile['G'] = [0 for i in range(k)]
	countTable = {}
	countTable['A'] = [1 for i in range(k)]
	countTable['T'] = [1 for i in range(k)]
	countTable['C'] = [1 for i in range(k)]
	countTable['G'] = [1 for i in range(k)]
	seq = {}
	with open('test.txt', 'r') as inputData:
		i = 0
		for line in inputData:
			line = line.strip()
			seq[i] = line
			i += 1
	# Initial the bestMotif and bestScore
	global SUM
	SUM = [0 for i in range(k)]
	bestProfile = profileBuilt(seq[0][0: k], k, profile, countTable)
	bestMotif = [seq[0][0: k]]
	for i in range(1, t):
		bestMotif.append(profileMost(seq[i], bestProfile, k))
		profile = profileBuilt(bestMotif[i], k, bestProfile, countTable)
	bestScore = hammingDistance(bestMotif, t)
	# Generate k-mers in first string seq[0]
	kmersInFirst = {}
	for i in xrange(len(seq[0]) - k + 1):
		kmersInFirst[seq[0][i: i + k]] = seq[0][i: i + k]
	for each in kmersInFirst:
		profile = {}
		# Reinitiation profile
		profile['A'] = [0 for i in range(k)]
		profile['C'] = [0 for i in range(k)]
		profile['T'] = [0 for i in range(k)]
		profile['G'] = [0 for i in range(k)]
		countTable = {}
		# Reinitiation countTable
		countTable['A'] = [1 for i in range(k)]
		countTable['T'] = [1 for i in range(k)]
		countTable['C'] = [1 for i in range(k)]
		countTable['G'] = [1 for i in range(k)]
		SUM = []
		# Reinitiation
		SUM = [0 for i in range(k)]
		motif = []
		motif = [kmersInFirst[each]]
		profile = profileBuilt(motif[0], k, profile, countTable)
		for i in range(1, t):
			motif.append(profileMost(seq[i], profile, k))
			profile = profileBuilt(motif[i], k, profile, countTable)
		score = hammingDistance(motif, t)
		if score < bestScore:
			bestMotif = motif
			bestScore = score
	for i in xrange(len(bestMotif)):
		print bestMotif[i]
	print bestScore


if __name__ == '__main__':
	main()
