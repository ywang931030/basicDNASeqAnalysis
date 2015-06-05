#!/usr/bin/env python
from random import Random


def random_str(randomlength):
	str = ''
	chars = 'ATCG'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str += chars[random.randint(0, length)]
	return str

randomLength = int(raw_input('length of the patterns:'))
print random_str(randomLength)
