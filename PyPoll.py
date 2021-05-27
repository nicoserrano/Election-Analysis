#Python Challenge

#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who receive votes
# 3. The total number of votes each candidate won. 
# 4. The percentage of votes each candidate won.
# 5. The winner of the election based on popular vote. 

# 6. Write the results in a text file to send to election commission

# Add dependencies
import csv
import os

# Assign a variable for load a file with direct path
file_to_load = './Resources/election_results.csv' #in VS Code. If in terminal from desktop pwd try:
#'Data Analytics/Data Bootcamp/Election-Analysis/Resources/election_results.csv'
# Assign a variable for load a file with direct path
file_to_save = 'Data Analytics/Data Bootcamp/Election-Analysis/Analysis/election_analysis.txt'

# Initialize a total vote counter
total_votes = 0 
# Initialize the candidate options list
candidate_options = []
# Initialize the candidate vote count dictionary
candidate_votes = {}
# Initiate variables for winning candidate
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    # Read and skip the header row.
    headers = next(file_reader) 
    # Print each row in the CSV file
    for row in file_reader:
        # Add the total vote count
        total_votes += 1
        #Print the candidate name in each row
        candidate_name = row[2]
        # Add the candidate name to the candidate list only if it is not repeated
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save results to text file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n" )
    print(election_results, end=" ")
    txt_file.write(election_results)


# 1. Print the total votes cast
print(total_votes)
# 2. Print the list of the candidates
print(candidate_options)
# 3. Print the candidate's vote count
print(candidate_votes)
# 4. Print the percentage of votes each candidate won
# Iterating through each candidate list 
for candidate_name in candidate_votes:
    # Retrieve vote values of each candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage for each candidate
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name with its percentage of the vote
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})')
# 5. The winner of the election
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning count = votes and winning % = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning candidate to the candidate's name. 
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"{'-'*30}\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"{'-'*30}\n")
print(winning_candidate_summary)