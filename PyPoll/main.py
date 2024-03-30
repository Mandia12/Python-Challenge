import os
import csv


total_votes = 0
candidates = []
votes_for_charles = 0
votes_for_diana = 0
votes_for_raymon = 0
all_data = []

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        all_data.append(row)
        
for vote in all_data:
    if vote[2] == candidates[0]:
        votes_for_charles += 1
    elif vote[2] == candidates[1]:
        votes_for_diana += 1
    else:
        vote[2] == candidates[2]
        votes_for_raymon += 1

vote_list = [votes_for_charles, votes_for_diana, votes_for_raymon]

percent_list = [round((vote / total_votes) * 100, 3) for vote in vote_list]

zipped_data = list(zip(candidates, percent_list, vote_list))

my_dict = {
    1: "Election Results", 
    2: "-------------------------", 
    3: f"Total votes: {total_votes}", 
    4: "-------------------------", 
    5: f"{zipped_data[0][0]}: {zipped_data[0][1]}% ({zipped_data[0][2]})", 
    6: f"{zipped_data[1][0]}: {zipped_data[1][1]}% ({zipped_data[1][2]})", 
    7: f"{zipped_data[2][0]}: {zipped_data[2][1]}% ({zipped_data[2][2]})", 
    8: "-------------------------", 
    9: f"Winner: {zipped_data[1][0]}", 
    10: "-------------------------"
    }

datafile = open("Analysis/Poll Analysis Results.txt", "w")
lines = [(my_dict[i+1] + "\n") for i in range(len(my_dict))]
datafile.writelines(lines)

for i in range(len(my_dict)):
    print(my_dict[i+1])