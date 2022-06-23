#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of cantidates who received votes.
#3. The percentage of votes each cantidate won.
#4. The total number of votes each cantidate won.
#5. The winner of the election based on popular vote.

#import dependencies

import csv
import os
from tkinter import W
from warnings import catch_warnings

#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote count

total_votes = 0

#Cantidate options and cantidate votes.
cantidate_options = []
#Declare an empty dictionary
cantidate_votes = {}

#Winning Cantidate and Winning count tracker
winning_cantidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:


    #To do: Read and analyze the data
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)

    for row in file_reader:

        #2. Add to the total vote count.
        total_votes += 1

        #Print the cantidate name for each row.
        cantidate_name = row[2]

        #If the cantidate does not match any existing cantidate.
        if cantidate_name not in cantidate_options:
            #Add it to the list of canitidates.
            cantidate_options.append(cantidate_name)

            #Begin tracking that cantidates vote count.
            cantidate_votes[cantidate_name] = 0

        cantidate_votes[cantidate_name] += 1

#iterate through the cantidate list.

for cantidate_name in cantidate_votes:
    #retrieve vout count of the cantidate
    votes = cantidate_votes[cantidate_name]
    #Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100


    #To do: print out each cantidates name, vote count, and percentage of votes to the terminal
    print(f"{cantidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        #if true then set the winning counts and votes
        winning_count = votes

        winning_percentage = vote_percentage

        winning_cantidate = cantidate_name

winning_cantidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_cantidate}\n"
    f"Winning Vote Count {winning_count:,}\n"
    f"Winning Percentage {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_cantidate_summary)

with open(file_to_save, "w") as txt_file:


    print()
