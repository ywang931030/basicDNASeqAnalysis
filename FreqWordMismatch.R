## Find Frequent k-mers patterns with d mismatches
## Input a string as reference genome, d as hamming distance and k as k-mers arguments
## Output the most frequent k-mers pattern within d-hamming-distance
## ========================= Functions ======================== ##


## ========================= Kernel ========================== ##

#Input
#Genome = scan(file.choose(), what = "")
#Test
Genome = "CGACACTAGAGGATGTGAGGGACCCACCGTACCGAAATCGACACTAGAAAACTATTGGGATGTGAGGGACCCACCGGATGTGAGGGACCCACCAAACTATTGGGATGTGAGAAACTATTGGGACCCACCGGATGTGAGGGATGTGAGAAACTATTGGGACCCACCGTACCGAAATAAACTATTGGTACCGAAATAAACTATTGGGACCCACCAAACTATTGCGACACTAGAAAACTATTGGGATGTGAGAAACTATTGGTACCGAAATGGATGTGAGGGATGTGAGGTACCGAAATGTACCGAAATCGACACTAGAAAACTATTGAAACTATTGGTACCGAAATAAACTATTGGGACCCACCGTACCGAAATGTACCGAAATGTACCGAAATGTACCGAAATGTACCGAAATGTACCGAAATGGATGTGAGGGACCCACCAAACTATTGGGATGTGAGGGATGTGAGGGATGTGAGGGACCCACCCGACACTAGAAAACTATTGGGATGTGAGAAACTATTGCGACACTAGACGACACTAGAGGACCCACCAAACTATTGCGACACTAGAGTACCGAAATGGACCCACCCGACACTAGAAAACTATTGGTACCGAAATGGACCCACCGGACCCACCGGATGTGAGGGATGTGAGGTACCGAAATGGATGTGAGGTACCGAAATGGACCCACCGGACCCACCGGATGTGAGAAACTATTGGTACCGAAATGGATGTGAGGTACCGAAATGGACCCACCGGACCCACCGGATGTGAGCGACACTAGAGGATGTGAGAAACTATTGAAACTATTGGTACCGAAATGTACCGAAATGGATGTGAGGGATGTGAGAAACTATTGGTACCGAAATGGATGTGAGGGATGTGAGGGACCCACCAAACTATTGCGACACTAGAAAACTATTGGGACCCACCAAACTATTG"
k = 6
d = 3
lengthGenome = nchar(Genome)
Genome = substring(Genome, seq(1,(lengthGenome - k + 1), by = 1), seq(k, lengthGenome, by = 1))
Patterns = Genome
Matching = c()
Freq = c()
for (i in 1 : length(Patterns)){
  Matching[length(Matching) + 1] = length(agrep(Patterns[i], Genome, max.distance = list(cost = d, insertions = 0, deletions = 0, subs = d)))
  Freq[length(Freq) + 1] = Patterns[i]
}
FreqWordMis = data.frame(Matching, Freq)
max = max(Matching)
FreqWordStat = as.vector(subset(FreqWordMis, FreqWordMis$Matching == max)$Freq)