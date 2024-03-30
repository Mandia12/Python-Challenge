# Python-Challenge

Description:

This repository contains two python scripts to organize, analyze, and present valuable information derived from their respective data sets. PyBank is a project that develops a financial analysis from records containing information on profit/losses and their corresponding dates. PyPoll is similar but accesses data from an election poll and generates an analysis on the outcome of the poll. Almost all the code was written on my own but I had to procure the writelines() method from an external source.

PyBank:

First, I imported the modules needed then created path to access csv file. After, I stored the header row and began looping through all following rows, accessing and calculating important values like total votes and total net. This loop also created lists with values that are utilized in the following code.

Using the list named "values", another list was created that contained the change from month to month. I then found the average from that list. 

From the list of changes just created and the list named "lists", I was able to locate the date at which the greatest increase and greatest decrease occurred. 

Now, having all values needed for the financial analysis, a dictionary was implemented to store and easily access the lines required in the analysis output. 

Lastly, I create, write in dictionary values, and place new file in desired directory, and print analysis to terminal.

PyPoll:

To acccess and manipulate data set, I import os and csv modules. Path is then set, file is opened, and header is stored. Following, the rows are looped through and critical values are collected including total votes, candidates, and rows.

Subsequently, a for loop is utilized to observe each row and compare the row's third value to the candidates, counting all votes for each candidate. Another list is instantiated containing the percentage of votes received for each candidate. The lists "candidates", "percent_list", and "vote_list" are zipped together. 

Then, a dictionary is created where all the values represent the lines for the final analysis. Some of these dictionary values access "zipped_data" via indexing to build the lines correctly.

Ultimately, a new txt. file is opened in write mode and the dictionary is employed to write the analysis into that file and to print the analysis into the terminal.

References:

For line 59 in PyBank and line 63 in PyPoll
https://www.geeksforgeeks.org/difference-between-write-and-writelines-function-in-python/#google_vignette
