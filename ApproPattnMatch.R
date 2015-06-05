##Approximate pattern matching
Genome = scan(file.choose(), what = "")
#Genome = "TTTAGAGCCTTCAGAGG"
Pattern = "GCTCAAG"
lengthGenome = nchar(Genome)
Distance = 3
k = nchar(Pattern)
Genome = substring(Genome, seq(1,(lengthGenome - k + 1), by = 1), seq(k, lengthGenome, by = 1))
Matching = agrep(Pattern, Genome, max.distance = list(cost = Distance, insertions = 0, deletions = 0, subs = Distance))
print(length(Matching))