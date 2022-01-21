import csv

rows = []

with open("gravity_merged_data.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

planet_data_rows = rows[1:]

suitable_planets = [];

for i in planet_data_rows:
    if float(i[2]) <= float(100) and float(i[5]) >= 150 and float(i[5]) <= 350:
        suitable_planets.append(i[1]);
        
print(suitable_planets);