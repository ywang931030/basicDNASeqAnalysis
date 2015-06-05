#!/usr/bin/env python
GLOBALPROFILE = {}


def profile(pattern):
    profile_value = 1.0
    profile = {}
    profile['A'] = [0.125, 0.25, 0.375]
    profile['C'] = [0.125, 0.125, 0.125]
    profile['G'] = [0.375, 0.375, 0.125]
    profile['T'] = [0.375, 0.25, 0.375]
    for i in xrange(len(pattern)):
        profile_value = profile_value * float(profile[pattern[i]][i])
    return profile_value


def main():
    # Read the input data.
    with open('test.txt', 'r') as input_data:
        seq = input_data.readline().strip()
        k, d = map(int, input_data.read().strip().split())
    all_kmers = {}
    for i in xrange(len(seq) - k + 1):
        all_kmers[seq[i: i + k]] = seq[i: i + k]
    # print all_kmers
    for each in all_kmers:
        GLOBALPROFILE[each] = profile(all_kmers[each])
    profile_most = max(GLOBALPROFILE.values())
    for each in all_kmers:
        if GLOBALPROFILE[each] == profile_most:
            print each            
if __name__ == '__main__':
    main()
