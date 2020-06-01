# Retrieve Data
# import os module for operating system independent path

import os
# import module for reading CSV files
import csv
# Assign a variable to the data file path
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to the save file path
file_to_save = os.path.join('analysis','election_analysis.txt')

# 1. Count the total number of votes
# 1a. Initialize total_votes to zero 
# and declare the list candidate_options and the dictionary candidate votes
total_votes = 0
candidate_options = []
candidate_votes = {}
# Open election data file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and headers row
    headers = next(file_reader)
    
    # Print each row in the election data file
    for row in file_reader:
        # Count the each vote instead of print(row)
        total_votes += 1

        # Get the candidate names
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Add new candidate to dictionary and initialize their vote count to zero
            candidate_votes[candidate_name]=0

        candidate_votes[candidate_name] += 1

# Save results to election_analysis.txt
with open(file_to_save,"w") as txt_file:

    # 1c. Print election results to terminal
    election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_results, end ="")
    txt_file.write(election_results)
    # 2. List of candidates that received votes
    #print(f'Candidates: {candidate_options}')

    # Set winner to the first candidate (update winner with for loop)
    # Set winning percentage to first candidate percentage
    winner = candidate_options[0]
    winning_percentage = (candidate_votes[candidate_options[0]]/total_votes)*100
        
    for candidates in candidate_options:
        # calculate the percentage of votes for each candidate
        percent_vote = (candidate_votes[candidates]/total_votes)*100
        # Save a summary of candidate results
        candidate_results = (f'{candidates}: {percent_vote:.1f}% ({candidate_votes[candidates]:,})\n')
        # Output candidate results to terminal
        print(candidate_results)
        # Write results to election_analysis.txt
        txt_file.write(candidate_results)
        # check if current candidate exceeds the vote total of current winner
        # if true update current winner and winning percentage
        if candidate_votes[candidates] > candidate_votes[winner]:
            winner = candidates
            winning_percentage = percent_vote

    # Save summary to winner_summary
    winner_summary = (
        f'-------------------------\n'
        f'Winner: {winner}\n'
        f'Winning vote count: {candidate_votes[winner]:,}\n'
        f'Winning percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    
    # Output summary to terminal
    print(winner_summary)
    # Write summary to election_analysis.txt
    txt_file.write(winner_summary)
