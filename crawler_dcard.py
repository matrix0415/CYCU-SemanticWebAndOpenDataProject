__author__ = 'Matrix'

import requests as req
import requesocks as reqs   # Tor, use py2
from os import listdir
from os.path import join as pathjoin
from multiprocessing import Pool

def checkNow():
	try:
		url ="https://www.dcard.tw/api/forum/all/1/"
		rs =req.get(url)
		latestID =rs.json()[0]['id']

	except Exception as e:
		print(e)

	return latestID


def storePage(paramater):
	try:
		folder, id =paramater
		# Tor ---
		session = reqs.session()
		session.proxies = {
			'http': 'socks5://127.0.0.1:9050',
			'https': 'socks5://127.0.0.1:9050'
		}
		url ="https://www.dcard.tw/api/post/all/%s"%id
		page =session.get(url)

		if page.status_code !=404:
			page.encoding ='utf-8'

			if page.content !='':
				with open(pathjoin(folder, "%s.json"%id), 'w') as f:
					f.write(str(page.content))
				print(id)

	except Exception as e:
		print(id, e)


if __name__ =='__main__':

	basepath ='/home/matrix/SemanticAndOpenData/Project/'
	output ='dataset/sources_dcard'
	fileList =sorted(listdir(pathjoin(basepath, output)))
	latest =checkNow()
	paramater =[(pathjoin(basepath, output), i) for i in range(latest-20000,latest)]# if "%s.json"%i not in fileList]
	print("Start!")

	pool =Pool(processes=120)
	pool.map(storePage, paramater)
	pool.close()
	pool.join()

	'''
	#----------------------------------------------------------------------------------------------
	from json import loads
	from os import path, listdir
	input = 'dataset/sources_dcard'
	output = 'dataset/afterFetch'
	datetimeSum = []
	data = [(fname, open(path.join(input, fname), 'r').read()) for fname in sorted(listdir(input))]
	data = [(fname, loads(i)) for fname, i in data if i != '']

	for fname, jsonobj in data:
		datetime = [i['version'][0]['createdAt'] for i in jsonobj['comment']]
		datetime.append(jsonobj['version'][0]['createdAt'])
		datetimeSum += datetime

		f = open(path.join(output, fname), 'w')
		f.write('\n'.join(datetime))
		f.close()
		print(fname)

	f = open(path.join(output, 'datetimeSum.dat'), 'w')
	f.write('\n'.join(datetimeSum))
	f.close()
	'''