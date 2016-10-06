# -*- coding: utf-8 -*-
__author__ = 'Matrix'

rs =[]
dataset ='dataset/ya.csv'
output ='dataset/ya_enhance.csv'

f =open(dataset, 'r').read().split('\n')

for word in set(f):
	tmp =0

	for content in f:
		if word ==content: tmp+=1

	rs.append("%s,%d"%(word, tmp))

s ="\n".join(rs)
f =open(output, 'w')
f.write(s)
f.close()
