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
				combos[combo].append(years[year][sellDay] / years[year][buyDay])
			else:
				combos[combo] = [years[year][sellDay] / years[year][buyDay]]	
			buyDay += 1
		sellDay += 1
maxCombo = ''
minCombo = ''
max = 0
min = 2
for combo in combos:
	average = 0
	for ratio in combos[combo]:
		average += ratio
	average /= len(combos[combo])
	if average > max:
		maxCombo = combo
		max = average
	if average < min:
		minCombo = combo
		min = average
print maxCombo + ' ' + str(max)
print minCombo + ' ' + str(min)
