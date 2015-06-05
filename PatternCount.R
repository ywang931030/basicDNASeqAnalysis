## Implement pattern counting
## input a sequence string and a pattern
## count numbers of pattern presented in the string
## For strings in r count from 1 not 0, so here we will count from 1 to |Text| - k + 1 rather than 0 to |Text| - k

## ========================================= Functions ===============================##
PatternCount <- function(SeqStr, Template){
  ## Input a string and store in a list 
  k = length(Template[[1]])
  count = 0
  ## Input Pattern, k is the length of pattern
  ## from 1 to |Text| - k + 1, compair strings and Pattern, if strings = pattern, add count, return count
  for (m in 1 : (length(SeqStr[[1]]) - k + 1)){
    if (all(SeqStr[[1]][m : (m + k - 1)] == Template[[1]][1 : k]) == TRUE){
      count = count + 1
    }
    
  } 
  count
}

## ========================================= Kernel =================================== ##
Text = scan(file.choose(), what = "")
Pattern = scan(file.choose(), what = "")
SeqStr <- strsplit(Text, "")
Template <- strsplit(Pattern, "")
count = PatternCount(SeqStr, Template)
print(count)

