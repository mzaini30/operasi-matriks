data = open('data.txt', 'r').read().splitlines()
data = [a.split("\t") for a in data]
print data