import os
import csv

total_votes = 0
candidate_list = []
candidate_votes = {}
new_vote = False
candidate_percent = {}
candidate_winner = "none"
candidate_winner_amount = 0

csv_file = os.path.join('election_data.csv')

with open(csv_file, 'r') as text:
    csvreader = csv.reader(text, delimiter = ',')

    csv_header = next(csvreader)

    for row in csvreader:
        
        # Counts total votes
        total_votes = total_votes + 1

        # Checks for new candidates and adds them to the vote list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes[row[2]] = 1
            new_vote = True
        
        # If no new candidates were just added, give the current vote to the specified candidate
        if new_vote is False:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        
        new_vote = False

# Calculates the percentage vote for each candidate and picks a winner based on that
for candidate in candidate_list:
    candidate_percent[candidate] = candidate_votes[candidate] / total_votes * 100

    if candidate_votes[candidate] > candidate_winner_amount:
        candidate_winner = candidate
        candidate_winner_amount = candidate_votes[candidate]

print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------")
for candidate in candidate_list:
    print(candidate + ": " + str(round(candidate_percent[candidate],3)) + "%  (" + str(candidate_votes[candidate]) + ")")
print("---------------------------")
print("Winner: " + candidate_winner)
print("---------------------------")
