#Imports modules needed to connect path and manipulate csv file
import os
import csv

#Sets path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Variable initialization
total_months = 0
total_net = 0
lists = []
values = []
changes = []
avgchange = 0
great_inc = 0
great_dec = 0
inc_date = ""
dec_date = ""

#Opens and ingests file into python
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Stores header row
    csv_header = next(csvreader)

#Loops through rows of cvsfile then calculates or collects
#number of months, total net profit/loss, lists containing either just values or entire rows
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        values.append(int(row[1]))
        lists.append(row)
    
#From the values list, this derives a list of changes and finds their average
changes = [x2 - x1 for (x1, x2) in zip(values, values[1:])]
avgchange = round((sum(changes)/len(changes)), 2)

#Calculates greatest increase/decrease and their corresponding dates
great_inc = max(changes)
great_dec = min(changes)
inc_date = lists[changes.index(great_inc)+ 1][0]
dec_date = lists[changes.index(great_dec) + 1][0]

#A dictionary created to store all lines for analysis result texts
my_dict = {
    1: "Financial Analysis",
    2: "----------------------------",
    3: f"Total Months: {total_months}", 
    4: f"Total: ${total_net}", 
    5: f"Average Change: ${avgchange}", 
    6: f"Greatest Increase in Profits: {inc_date} (${great_inc})", 
    7: f"Greatest Decrease in Profits: {dec_date} (${great_dec})"
    }

#Opens a file to write to, creates a list of lines, then writes lines in new txt. file
datafile = open("Analysis/Bank Analysis Results.txt", "w")
lines = [(my_dict[i+1] + "\n") for i in range(len(my_dict))]   
datafile.writelines(lines)

#Finally prints results in terminal
for i in range(len(my_dict)):
    print(my_dict[i+1])