## Input a sequence string
## translate it and output in 5-3 direction
## Output a rerverse complement string

## ==================================== Function =================================== ##

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

## =================================== Kernel ====================================== ##
## Input
#Seq = scan(file.choose(), what = "")
## test
Seq = "AAAACCCGGT"
Seq = strsplit(Seq, "")
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
print (ReSeq)

