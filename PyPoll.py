#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of cantidates who received votes.
#3. The percentage of votes each cantidate won.
#4. The total number of votes each cantidate won.
#5. The winner of the election based on popular vote.

#import dependencies

import csv
import os

#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:


    #To do: Read and analyze the data
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)

    print(headers)

with open(file_to_save, "w") as txt_file:


    print()
