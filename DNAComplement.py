#!/usr/bin/env python
from string import maketrans
file = open('test.txt', 'r')
DNAStri = file.read()
## maketrans(inputtab,outputtab)
#DNATab = maketrans('ATCG','TAGC')
#DNACom = DNAStri.translate(DNATab)
## reverse the string DNACom[begin:end:step]
#print DNACom[::-1]
## more briefly
print(DNAStri[::1].translate(maketrans('ATCG','TAGC')))


