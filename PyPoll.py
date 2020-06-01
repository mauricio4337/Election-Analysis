# Retrieve Data
# import os module for operating system independent path


import os
# import module for reading CSV files
import csv
# Assign a variable to the data file path
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to the save file path
file_to_save = os.path.join('.','analysis','election_analysis.txt')

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

    # 1c. Print the total votes
    print(f'Total votes counted: {total_votes:,}')
    # 2. List of candidates that received votes
    print(f'Candidates: {candidate_options}')
    # 3. The total number of votes that each candidate received
    winner = candidate_options[0]
    winning_percentage = 0
    for candidates in candidate_options:
        percent_vote = (candidate_votes[candidates]/total_votes)*100
        print(f'{candidates}: {percent_vote:.1f}% ({candidate_votes[candidates]:,})\n')
        if candidate_votes[candidates] > candidate_votes[winner]:
            winner = candidates
            winning_percentage = percent_vote

    winner_summary = (
        f'-------------------------\n'
        f'Winner: {winner}\n'
        f'Winning vote count: {candidate_votes[winner]:,}\n'
        f'Winning percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    
    print(winner_summary)

# 4. Percent of the vote that each candidate received
# 5. Determine the winner of the election