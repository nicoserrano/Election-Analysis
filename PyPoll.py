#Python Challenge

#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who receive votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won. 
# 5. The winner of the election based on popular vote. 


import csv
import os
#Assign a variable for the file to load and the path
file_to_load = 'Data Analytics/Data Bootcamp/Election-Analysis/Resources/election_results.csv'
#open the election results and read the file
with open(file_to_load) as election_data: 
    #print the file data
    print(election_data) #not necessary in the election analysis
    #read and analyze the data
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row) #this fct print all the csv in the terminal. Not necessary in the election analysis

    #skip the header row
    headers = next(file_reader)
    print(headers)





#create a filename variable to a direct or indirect path to the file
file_to_save = 'Data Analytics/Data Bootcamp/Election-Analysis/Analysis/election_analysis.txt'
outfile = open(file_to_save,"w")
#write some data to the file
outfile.write("Hello World")
outfile.close()

#Other and more clean to do it
with open(file_to_save,"w") as txt_file:
    txt_file.write("Hello World x2") #it replaces the hello world we wrote above
     # Write three counties to the file.

with open(file_to_save,"w") as txt_file:
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
