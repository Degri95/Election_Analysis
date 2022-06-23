#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

#import dependencies

import csv
import os


#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote count

total_votes = 0

#Candidate options and candidate votes.
candidate_options = []
#Declare an empty dictionary
candidate_votes = {}

#Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    for row in file_reader:

        #2. Add to the total vote count.
        total_votes += 1

        #Print the candidate name for each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            #Add it to the list of canitidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1



with open(file_to_save, "w") as txt_file:

    #Print the final vote counnt to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    
    #Save the final vote count to the text file.
    txt_file.write(election_results)


    #iterate through the candidate list.
    for candidate_name in candidate_votes:
        #retrieve vout count of the candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100


        #Print out each candidates name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            #if true then set the winning counts and votes
            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name
   
    #print(winning_candidate_summary)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count {winning_count:,}\n"
        f"Winning Percentage {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #Sae the winning canditate's resusts to the text file.
    txt_file.write(winning_candidate_summary)
    

    