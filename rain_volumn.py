__author__ = 'Matrix'
import numpy as np
import requests as req
from bs4 import BeautifulSoup

if __name__ =='__main__':
	location =[i.split(',') for i in """466950, 彭佳嶼
		466940,基隆
		466920,臺北
		466910,鞍部
		466930,竹子湖
		466900,淡水
		466880,板橋
		C0C520,桃園
		467050,新屋
		467571,新竹
		C1E770,苗栗
		467490,臺中
		467770,梧棲
		C1G631,彰化
		467650,日月潭
		C1K310,雲林
		467480,嘉義
		467530,阿里山
		467550,玉山
		467410,臺南
		467440,高雄
		C0R170,屏東
		467590,恆春
		467080,宜蘭
		467060,蘇澳
		466990,花蓮
		467610,成功
		467660,臺東
		467540,大武
		467620,蘭嶼
		467990,馬祖
		467110,金門
		467350,澎湖
		467300,東吉島""".replace('\t', '').split('\n')]

	urldata =[(year, i[1], 'http://www.cwb.gov.tw/V7/climate/dailyPrecipitation/Data/%s_%s.htm'%(i[0], year))
	        for year in [2014, 2015] for i in location
	      ]

	rainvolumn = [(year, location, req.get(url).text) for year, location, url in urldata]
	dset =[]
	rs =[]

	for year, location, htmltable in rainvolumn:
		data =np.array([[cell.text for cell in row("td")] for row in BeautifulSoup(htmltable)("tr")[3:-2]])
		data[data == ''] ='0'
		data[data == '-'] = '0'
		data[data == 'T'] = '0'
		data[data == 'X'] = '0'
		data =data.astype(np.float).T

		for month, field in enumerate(data):
			for day, value in enumerate(field):
				rs.append("%s-%s-%s,%s,%s"%(year, month+1, day+1, location, value))

	f =open("rainvolumn.csv", 'w')
	f.write("\n".join(rs))
	f.close()