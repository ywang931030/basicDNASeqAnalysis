## Find Frequent k-mers patterns, including their reverse pattern, with d mismatches
## Input a string as reference genome, d as hamming distance and k as k-mers arguments
## Output the most frequent k-mers pattern within d-hamming-distance
## ========================= Functions ======================== ##
## Pairs
SeqPair <- function(InputSeq){
  if (InputSeq == 'A' || InputSeq == 'T'){
    CompSeq = if (InputSeq == 'A') 'T' else 'A'
  }
  else{
    CompSeq = if(InputSeq == 'C') 'G' else 'C'
  }
  CompSeq
}

Complete <- function(Seq){
  PairedSeq = list()
  ReSeq = c()
  Seq = strsplit(Seq, "")[[1]]
  for (i in 1: length(Seq)){
    PairedSeq[length(PairedSeq) + 1] = SeqPair(Seq[i])
  }
  j = length(PairedSeq)
  
  ## Reverse the seq to 5-3 direction
  while ( j >= 1){
    ReSeq[length(ReSeq) + 1] = PairedSeq[[j]]
    j = j - 1
  }
  ReSeq = paste(ReSeq, collapse = "")
    
}

## ========================= Kernel ========================== ##

#Input
#Genome = scan(file.choose(), what = "")
#Test
Genome = "CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT"
k = 9
d = 3
lengthGenome = nchar(Genome)
Genome = substring(Genome, seq(1,(lengthGenome - k + 1), by = 1), seq(k, lengthGenome, by = 1))
Patterns = Genome
Matching = c()
FreqPattern = c()
FreqRePattern = c()
for (i in 1 : length(Patterns)){
  RePattern = Complete(Patterns[i])
  #print (RePattern)
  PatNum = agrep(Patterns[i], Genome, max.distance = list(cost = d, insertions = 0, deletions = 0, subs = d))
  RePatNum = agrep(RePattern, Genome, max.distance = list(cost = d, insertions = 0, deletions = 0, subs = d)) 
  Num = c(PatNum, RePatNum)
  Matching[length(Matching) + 1] = length(Num)
  FreqPattern[length(FreqPattern) + 1] = Patterns[i]
  FreqRePattern[length(FreqRePattern) + 1] = RePattern
}
FreqWordMis = data.frame(Matching, FreqPattern, FreqRePattern)
max = max(Matching)
FreStatP = as.vector(subset(FreqWordMis, FreqWordMis$Matching == max)$FreqPattern)
FreStatR = as.vector(subset(FreqWordMis, FreqWordMis$Matching == max)$FreqRePattern)
FreqWordStat = c(FreStatP, FreStatR)

print(FreqWordStat)

