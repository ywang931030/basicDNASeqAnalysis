#!/usr/bin/env python
SEQ = {}


from collections import defaultdict
from itertools import combinations, product, izip


def freqWordWithMismatches(seq, k, d):
    kmerFreq = defaultdict(int)
    for i in xrange(len(seq) - k + 1):
        kmerFreq[seq[i: i + k]] += 1
    mismatchCount = defaultdict(int)
    for kmer, freq in kmerFreq.iteritems():
        for mismatch in kmersMismatches(kmer, d):
            mismatchCount[mismatch] += freq
    return [kmer for kmer, count in mismatchCount.iteritems()]


def kmersMismatches(kmer, d):
    mismatches = [kmer]
    altBase = {'A': 'CTG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
    for dist in xrange(1, d + 1):
        for changeIndices in combinations(xrange(len(kmer)), dist):
            for substitutions in product(*[altBase[kmer[i]] for i in changeIndices]):
                newMismatch = list(kmer)
                for idx, sub in izip(changeIndices, substitutions):
                    newMismatch[idx] = sub
                mismatches.append(''.join(newMismatch))
    return mismatches


def main():
    with open('test.txt', 'r') as inputData:
        global SEQ
        i = 1
        for line in inputData:
            line = line.strip()
            SEQ[i] = line
            i += 1
    allKmers = {}
    freqAllKmers = {}
    for each in SEQ:
        allKmers[SEQ[each]] = freqWordWithMismatches(SEQ[each], 5, 1)
    for each in allKmers:
        for i in xrange(len(allKmers[each])):
            freqAllKmers[allKmers[each][i]] = 0
    for each in freqAllKmers:
        for kmers in allKmers:
            for j in xrange(len(allKmers[kmers])):
                if each == allKmers[kmers][j]:
                    freqAllKmers[each] += 1
        if freqAllKmers[each] == 6:
            print each

if __name__ == '__main__':
    main()
