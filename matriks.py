import numpy as np, os

data = open('data.txt', 'r').read().splitlines()
data = [a.split("\t") for a in data]

data = np.array(data).T
# print data

hasil = open('hasil.txt', 'w')
for a, b in enumerate(data):
	for c, d in enumerate(data[a]):
		hasil.write(d)
		hasil.write('\t')
	hasil.write('\n')

print 'Selesai.'
os.system("pause")