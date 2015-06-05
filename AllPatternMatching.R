## Input a pattern and a genome
## reverse and transcript the pattern as a new pattern, we will compair both new one and origin one to the genome
## output all positions those substrings appeared to occur

## ==================================== Functions ================================ ##

## ReversePairs
SeqPair <- function(InputSeq){
  if (InputSeq == 'A' || InputSeq == 'T'){
    CompSeq = if (InputSeq == 'A') 'T' else 'A'
  }
  else{
    CompSeq = if(InputSeq == 'C') 'G' else 'C'
  }
  CompSeq
}

## ReverseComplement

ReverseComplement <- function(InputString){
  Seq = strsplit(InputString, "")
  PairedSeq = list()
  ReSeq = c()
  for (i in 1: length(Seq[[1]])){
    PairedSeq[length(PairedSeq) + 1] = SeqPair(Seq[[1]][i])
  }
  j = length(PairedSeq)
  
  ## Reverse the seq to 5-3 direction
  while ( j >= 1){
    ReSeq[length(ReSeq) + 1] = PairedSeq[[j]]
    j = j - 1
  }
  ReSeq = paste(ReSeq, collapse = "")
  ReSeq  
}

## PatternPostion to show the position of the appeared substrings
PatternPosition <- function(SeqStr, Template){
  ## Input a string and store in a list 
  k = length(Template[[1]])
  Position = c()
  ## Input Pattern, k is the length of pattern
  ## from 1 to |Text| - k + 1, compair strings and Pattern, if strings = pattern, add count, return count
  for (m in 1 : (length(SeqStr[[1]]) - k + 1)){
    if (all(SeqStr[[1]][m : (m + k - 1)] == Template[[1]][1 : k]) == TRUE){
      Position[length(Position) + 1] = m - 1
    }  
  } 
  Position
}

## =================================== Kernel =============================== ##

## Input
#Genome = scan(file.choose(), what = "")
## Test
Genome = "GATATATGCATATACTT"
OriPattern = "ATAT"
RevPattern = ReverseComplement (OriPattern)
AllPosition = c()
Genome = strsplit(Genome, "")
OriPattern = strsplit(OriPattern, "")
RevPattern = strsplit(RevPattern, "")
OriPosition = PatternPosition(Genome, OriPattern)
RevPosition = PatternPosition(Genome, RevPattern)
## Combine two position record to one and remove the repeat
AllPosition = unique(sort(c(OriPosition, RevPosition)))
print(AllPosition)
