## Input squence files and length of detecting pattern
## Output the most frequent pattern in sequence strings


## ========================================== Functions ======================================= ##

## Detect the presented patterns
## Attention: input of the function must be list
PatternCount <- function(SeqStr, Template){
  ## Input a string and store in a list 
  k = length(Template)
  count = 0
  ## Input Pattern, k is the length of pattern
  ## from 1 to |Text| - k + 1, compair strings and Pattern, if strings = pattern, add count, return count
  for (m in 1 : (length(SeqStr[[1]]) - k + 1)){
    if (all(SeqStr[[1]][m : (m + k - 1)] == Template[1 : k]) == TRUE){
      count = count + 1
    }
    
  } 
  count
}

## Detect the most frequent patterns
FrequentWords <- function(Text, k){
  #FrequentPatterns <- data.frame()
  Count <- c()
  AllPattern <- c()
  for (i in 1 : (length(Text[[1]]) - k + 1)){
    Pattern = Text[[1]][i:(i + k - 1)]
    #Count[length(Count) + 1] <- PatternCount(Text, Pattern)
    ## Paste the elements in the list back to a string, so that a data frame can hold both of count and pattern
    AllPattern[[length(AllPattern) + 1]] <- paste(Pattern, collapse = "")
  }
  #maxCount = max(Count)
  #FrequentPatterns <- data.frame(Count, AllPattern) 
  #FrequentPatterns
  AllPattern
}



## ========================================== Kernel ======================================== ##
## Input
#Text = scan(file.choose(), what = "")

## Test
Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = list(A = c(0.2, 0.2, 0.3, 0.2, 0.3), T = c(0.4, 0.3, 0.1, 0.5, 0.1), G = c(0.3, 0.3, 0.5, 0.2, 0.4), C = c( 0.1, 0.2, 0.1, 0.1, 0.2))
## Convert into list
Text = strsplit(Text, "")
FreqList <- FrequentWords(Text, k)
print (FreqList)
