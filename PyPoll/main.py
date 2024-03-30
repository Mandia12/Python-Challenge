import os
import csv


total_votes = 0
candidates = []


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

print(total_votes)
print(candidates)