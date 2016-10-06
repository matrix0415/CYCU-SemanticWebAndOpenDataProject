

if __name__ =='__main__':
	countData =[]
	countNumber =[]
	f =open('dataset/export2.csv', 'r').read().split('\n')[10:-10]
	print(len(f))
	content =[i.split(',')[3:5] for i in f]


	for c in content:
		if c not in countData:
			countData.append(c)
			countNumber.append(content.count(c))

	print(len(countData))
	print(len(countNumber))
	print(countData)
	print(countNumber)

	from sklearn import svm

	clf = svm.SVR()
	clf.fit(countData, countNumber)
	print(clf.predict([100, 0]))