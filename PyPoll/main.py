import os
import csv

csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')

numbervotes=0
candidates = {}
winner= ""



with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        numbervotes+=1
        names = row[2]
    if names in candidates:
        candidates[names] += 1
    else:
        candidates[names] = 1


for candidate in candidates:
    print(candidate)

print(f'''Election Results
---------------------------------
Total Votes: {numbervotes}
---------------------------------''')
##