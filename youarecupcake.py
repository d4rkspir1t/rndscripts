#!/usr/bin/env python
import sys

def fetch(arguments,index):
	try:
		res = arguments[index]
	except IndexError:
		res = 0
	return res

lv = 'Cupcake'

arguments =[item.lower() for item in sys.argv[1:]]
# print(arguments)
# print(fetch(arguments, 1))
# print(fetch(arguments, 2))
# print(fetch(arguments, 3))
if fetch(arguments, 1) == 'love':
    if fetch(arguments, 2) == lv.lower():
        print('Of course, she\'s so cool even The Economist wants her')
    else:
        print('No! You love %s. SAYIT!' % (lv.capitalize()))
else:
    print('C\'mon, talk about love, bearbrain. I know it\'s hard to get out.')
