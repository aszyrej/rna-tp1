import csv

def readDataEj1(file_name):
	benignos = []
	malignos = []
	with open(file_name, 'rb') as csvfile:
		rows = csv.reader(csvfile, delimiter=',')
		for row in rows:
			if row[0] == 'M':
				malignos.append(row)
			else: 
				benignos.append(row)
	if len(benignos) >= len(malignos):
		benignos = benignos[0:len(malignos)]
	else:
		malignos = malignos[0:len(benignos)]
	return benignos, malignos
