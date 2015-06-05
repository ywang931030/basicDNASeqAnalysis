#!/usr/bin/env python
SEQ = {}


import distance


def dis(kmers, ownKmers):
    hammingDistance = {}
    minDistance = 0
    for each in ownKmers:
        hammingDistance[each] = []
        for i in xrange(len(ownKmers[each])):
            hammingDistance[each].append(distance.hamming(kmers, ownKmers[each][i]))
    for each in hammingDistance:
        minDistance += min(hammingDistance[each])
    return minDistance


def main():
    with open('test.txt', 'r') as inputData:
        global SEQ
        i = 1
        for line in inputData:
            line = line.strip()
            SEQ[i] = line
            i += 1
        allKmers = {}
        k = 7
        for each in SEQ:
            for i in xrange(len(SEQ[each]) - k + 1):
                allKmers[SEQ[each][i: i + k]] = 0
        ownKmers = {}
        for each in SEQ:
            ownKmers[SEQ[each]] = []
            for i in xrange(len(SEQ[each]) - k + 1):
                ownKmers[SEQ[each]].append(''.join(SEQ[each][i: i + k]))
        for kmers in allKmers:
            allKmers[kmers] = dis(kmers, ownKmers)
            median = min(allKmers.values())
        for kmers in allKmers:
            if allKmers[kmers] == median:
                print kmers


if __name__ == '__main__':
    main()
