## Calculate the number of G C bases in genomes of length i
## Input genomes
## output skew(genome) from 1 to i
## ====================== Functions =========================== ##

## ====================== Kernel =========================== ##
## Build a punish vector
# test
Genome = "GATACACTTCCCGAGTAGGTACTG"
# input
#Genome = scan(file.choose(), what = "")
Genome = strsplit(Genome, "")[[1]]
Genome = gsub(pattern = "A|T", replacement = 0, Genome)
Genome = gsub(pattern = "G", replacement = 1, Genome)
Genome = gsub(pattern = "C", replacement = -1, Genome)
Score = as.numeric(Genome)
Skew = c()
Skew[1] = Score[1]
for (j in 1 : length(Score)){
  if (Score[j] == 0 ){
    Skew[length(Skew) + 1] = Skew[length(Skew)]
  }
 else{
  Skew[length(Skew) + 1] = sum(Score[0:j]) 
 }
}

print(grep(min(Skew),Skew) - 1)
