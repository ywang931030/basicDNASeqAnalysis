pattern = "GCGGCCGCT"
repattern = "AGCGGCCGC"
Genome = "CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT"
k = 9
d = 3
lengthGenome = nchar(Genome)
Genome = substring(Genome, seq(1,(lengthGenome - k + 1), by = 1), seq(k, lengthGenome, by = 1))
Patterns = Genome
MatchingP = length(agrep(pattern, Genome, max.distance = list(cost = d, insertions = 0, deletions = 0, subs = d)))
Freq = agrep(pattern, Genome, max.distance = list(cost = d, insertions = 0, deletions = 0, subs = d), value = T)
MatchingR = length(agrep(repattern, Genome, max.distance = list(cost = d, insertions = 0, deletions = 0, subs = d)))
FreqP = pattern
FreqR = repattern
print(MatchingP + MatchingR)
print(Freq)