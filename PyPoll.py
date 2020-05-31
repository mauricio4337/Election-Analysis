# Retrieve Data
# import os module for operating system independent path


import os
# import module for reading CSV files
import csv
# Assign a variable to the data file path
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to the save file path
file_to_save = os.path.join('.','analysis','election_analysis.txt')

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print headers row
    headers = next(file_reader)
    print(headers)
    
    #for row in file_reader:
    #    print(row)

# 1. Count the total number of votes
# 2. List of candidates that received votes
# 3. The total number of votes that each candidate received
# 4. Percent of the vote that each candidate received
# 5. Determine the winner of the election