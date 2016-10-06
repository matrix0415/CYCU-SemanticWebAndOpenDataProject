# -*- coding: utf-8 -*-
__author__ = 'Matrix'

from os import listdir
from os.path import join as joinpath

from jieba import cut, suggest_freq
from bs4 import BeautifulSoup as bs

location =[]
inputLoc ='dataset/sources'
outputLoc ='dataset/ya.csv'

wf =open(outputLoc, 'a', encoding='utf-8')
try:
	rf =open(outputLoc, 'r', encoding='utf-8').read()
	location =rf.split('\n')
	[add_word(w) for w in location]
	print(location)

except:
	print("No file.")

print("Start")

for count in range(0, 3000, 100):
	print("Round %d!! -------------"%count)

	try:
		f =[bs(open(joinpath(inputLoc, fname), 'r', encoding='utf-8')).select("div.box_2")[0].text for fname in listdir(inputLoc)[count:count+100]]
		print("File load.")
		token =[rs.split('）')[0].replace('\n', '').replace('\t', '').replace('（', '') for rs in f]
		print("Words Preprocess")
	except:
			continue

	for key, t in enumerate(token):
		a =[(key,a) for key, a in enumerate([s for s  in cut(t)])]
		print(key, a)
		loc =[i for key, i in a if i in location]

		if not loc:
			locationKey =input("Location? (10==renew) ")
			try:
				location.append(a[int(locationKey)][1])
				f.write("%s\n"%a[int(locationKey)][1])

			except:
				print("None location.")

				if int(locationKey)==10:
					locName =input("Location Name: ")
					suggest_freq(locName)
					location.append(locName)
					wf.write("%s\n"%locName)

		else:
			location.append(loc[0])
			wf.write("%s\n"%loc[0])

wf.close()








'''
try:
	rs =content.select("div.box_2")[0].text
	title =rs.split('）')[0].replace('\n', '').replace('\t', '').replace('（', '')
	string =ba.cut(title)
	print([k for k in string])
except:
	pass
'''
