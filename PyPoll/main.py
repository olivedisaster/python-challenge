#Modules
import os
import csv

election = "Desktop/Bootcamp/Homework/HW 2/python-challenge/PyPoll/Resources/election_data.csv"

#Set file path
csvpath = os.path.join("Resources","election_data.csv")

#Define Variables
votes_tot = 0
cand_rec_vote = 0
percent_vote = 0

#Set empty dictionary
candidates = {}

#Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votes_tot = votes_tot + 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.update({candidate : 1})
        
        else:
            candidates[candidate] += 1

    print(candidates)

print("Election Results")
print("__________________________")
print(f"Total Votes: {votes_tot}")
print("__________________________")

winner_name = ""
winner = 0

for candidate in candidates:
    print("{candidate}: {candidates[candidate]/votes_tot)*100:.3f}% ({candidates[candidate]})")
    if candidates[candidate] > winner:
        winner = candidates[candidate]
        winner_name = candidate
print("_________________________")
print(f"Winner: {winner_name}")
output_path = os.path.join("analysis", "Election_Results_Analysis.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f"Total Votes: {votes_tot}"])
    csvwriter.writerow(['-----------------------------'])
    for candidate in candidates:
        csvfile.write(f"{candidate}: {(candidates[candidate]/votes_tot)*100:.3f}% ({candidates[candidate]})\n")
    csvfile.write("---------------------------\n")
    csvfile.write(f"Winner: {winner_name}\n")
    csvfile.write("---------------------------\n")
  


