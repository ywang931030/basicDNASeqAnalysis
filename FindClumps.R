## Find all clumps in a genome
## input a genome string and integer L, k, t
## output all distinct k-mers forming (L,t)-clumps in Genome
## Clumps - if there is an interval of Genome of length L in which this k-mer appears at least t times

## ============================================= Functions =========================================== ##

## ============================================ Kernel ============================================= ##
##Input
Genome = scan(file.choose(), what = "")
Pattern = Genome
#print ("Enter k")
#k = readline("")
#print ("Enter L")
#L = readline("")
#print ("Enter t")
#t = readline("")
##test
#Genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k = 9
L = 500
t = 3
#Pattern = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
lengthGenome = nchar(Genome)
Genome = substring(Genome, seq(1,(lengthGenome - k + 1), by = 1), seq(k, lengthGenome, by = 1))
Pattern = substring(Pattern, seq(1,(lengthGenome - k + 1), by = 1), seq(k, lengthGenome, by = 1))
Pattern = as.data.frame(table(Pattern))
FreqPattern = as.vector(Pattern[Pattern$Freq >= t,]$Pattern)
numFreq = length(FreqPattern)
LtClumps <- c()
for (i in 1 : numFreq){
  Position <- grep(FreqPattern[i], Genome)
  if ((Position[t] - Position[1] + k - 1) <= L){
    LtClumps[length(LtClumps) + 1] <- FreqPattern[i]
  }
}
print(length(LtClumps))
## split the genome in a list c.f. read frame
## Find the frequentwords, use function FrequentWords(Text, k)
## c.f. output the count of the patterns and their reversecomplement, use function AllPatternMatching(Genome, oriPattern)
## save the pattern which occur more than t times, as well as the every position of the occurance
#print(LtClumps(Genome, k, L, t))
## detect whether the pattern is (L,t)-clumps
## if length from the first position of the occurance to the last character of t time occurance position <= L
## then we consider it a (L,t)-clumps