import os
import csv

csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')

numbervotes=0
candidates = []
winner= ""



with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)


    for row in csvreader:
        numbervotes+=1
        names = row[2]

        if names in candidates:
            continue
        else:
            candidates.append(names)


print(candidates)



print(f'''Election Results
---------------------------------
Total Votes: {numbervotes}
---------------------------------''')
for candidate in candidates:
    candidate_votes = sum(1 for row in csv.reader(open(csvpath)) if row[2] == candidate)
    percentage = (candidate_votes / numbervotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes})")

##