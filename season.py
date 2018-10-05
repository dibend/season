import csv
import sys

years = {}

with open(sys.argv[1], 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		year = int(row[0][:4])
		close = float(row[5])
		if year in years:
			years[year].append(close)
		else:
			years[year] = [close]
combos = {}
for year in years:
	days = len(years[year])
	sellDay = 1
	while sellDay < days:
		buyDay = 0
		while buyDay < sellDay:
			combo = str(buyDay) + ' ' + str(sellDay)
			if combo in combos:
				combos[combo].append(years[year][buyDay] / years[year][sellDay])
			else:
				combos[combo] = [years[year][buyDay] / years[year][sellDay]]	
			buyDay += 1
		sellDay += 1
max = 0
for combo in combos:
	average = 0
	for percent in combos[combo]:
		average += percent
	average /= len(combos[combo])
	if average > max:
		print combo
		print average
		max = average
