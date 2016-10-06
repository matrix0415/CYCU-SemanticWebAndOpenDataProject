__author__ = 'Matrix'
from json import loads
from os import path, listdir

def jsonloads(file):
	try:
		return loads(file)
	except Exception as e:
		print(e)


if __name__ =='__main__':
	input ='dataset/sources_dcard'
	output ='dataset/afterFetch'
	datetimeSum =[]
	outputlist =[x for x in listdir(output)]
	data = [fname for fname in sorted(listdir(input))]# if fname not in outputlist]

	#if path.isfile(path.join(output, 'datetimeSum.dat')):
	#	datetimeSum =open(path.join(output, 'datetimeSum.dat'), 'r').read().split('\n')

	for fname in data:
		jsonobj =jsonloads(open(path.join(input, fname), 'r').read())

		if None != jsonobj and 'comment' in jsonobj:
			datetime =[(i['version'][0]['createdAt'], i['member']['school']) for i in jsonobj['comment']]
			datetime.append((jsonobj['version'][0]['createdAt'], jsonobj['member']['school']))
			datetime =["%s,%s"%("%s %s"%(i.split('T')[0], i.split('T')[1].split('.')[0]), school)
			           for i, school in datetime if school != "匿名" and school !="一個把留言刪除的同學"]
			datetimeSum +=datetime

			f =open(path.join(output, fname), 'w')
			f.write('\n'.join(datetime))
			f.close()
			print(fname)

	f =open(path.join(output, 'datetimeSum.dat'), 'w')
	f.write('\n'.join(sorted(datetimeSum)))
	f.close()
