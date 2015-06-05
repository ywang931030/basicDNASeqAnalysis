#!/usr/bin/env python
file = open('test.txt', 'r')
DNAString = file.read()
## replace 'T' with 'U', here we use function replace
RNAString = DNAString.replace('T', 'U')
print RNAString