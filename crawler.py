# -*- coding: utf-8 -*-
__author__ = 'Matrix'

import jieba as ba
import requests as req
from bs4 import BeautifulSoup as bs
from os.path import join as pathjoin
from multiprocessing import Pool

def storePage(paramater):
	year, month, date, idList, folder=paramater

	for id in idList:
		count =0
		url ="http://www.cna.com.tw/news/aopl/%d%0.2d%0.2d5%0.3d-1.aspx"%(year, month, date, id)
		filename =url.split('/')[5]
		page =req.get(url)
		page.encoding ='utf-8'
		content =bs(page.text)

		if not content.body.findAll(text ="查無此新聞!!"):
			content =str(content.body).replace('\n',' ').replace('\t', ' ').replace('   ', ' ').replace('  ', ' ')
			f =open(pathjoin(folder, filename), 'w')
			f.write(content)
			f.close()
			print(filename)
		else:
			break


if __name__ =='__main__':
	output ='dataset/sources'
	#   http://www.cna.com.tw/news/aopl/201504260001-1.aspx
	#   http://www.cna.com.tw/news/aopl/201504265001-1.aspx
	pool =Pool(processes=20)
	yearList =range(2013, 2016)
	monthList =range(1,13)
	dateList =range(1,30)
	newsIDList =range(2,500)
	paramater =[(y, k, i, newsIDList, output) for y in yearList for k in monthList for i in dateList]

	pool.map(storePage, paramater)
	pool.close()
	pool.join()

	'''
		try:
			rs =content.select("div.box_2")[0].text
			title =rs.split('）')[0].replace('\n', '').replace('\t', '').replace('（', '')
			string =ba.cut(title)
			print([k for k in string])
		except:
			pass
	'''