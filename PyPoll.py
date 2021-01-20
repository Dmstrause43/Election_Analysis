# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#import datetime

#now = datetime.datetime.now()

#print("The time right now is ", now)

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
#file_to_load = 'Resources\election_results.csv'
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")

    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)


#print(winning_candidate_summary)
            
#print(candidate_votes)

#print(candidate_options)
# print(total_votes)


    #for row in file_reader:
    #    print(row)

#with open(file_to_save, 'w') as text_file:

    #text_file.write("Hello World")
    #text_file.write("Arapahoe, ")
    #text_file.write("Denver, ")
    #text_file.write("Jefferson, ")
    #text_file.write("Arapahoe, Denver, Jefferson")
    #text_file.write("Arapahoe\nDenver\nJefferson")
#outfile.write('Hello World')

#outfile.close()

#with open(file_to_load) as election_data:
#    print(election_data)

#election_data = open(file_to_load, 'r')

#election_data.close()
#electionResults = open(election_results.csv, "r")
