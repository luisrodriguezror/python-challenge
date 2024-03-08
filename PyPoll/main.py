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


winpercentage=0
winner=""

print(f'''Election Results
---------------------------------
Total Votes: {numbervotes:,}
---------------------------------''')
for candidate in candidates:
    candidate_votes = sum(1 for row in csv.reader(open(csvpath)) if row[2] == candidate)
    percentage = (candidate_votes / numbervotes) * 100
    print(f"{candidate}: {percentage:.2f}% ({candidate_votes:,})")

    if percentage > winpercentage:
        winpercentage=percentage
        winner=candidate
print('---------------------------------')
print(f'''Winner: {winner}
---------------------------------''')

output_path = os.path.join("PyPoll", "analysis", "analysis_result.txt")

output_path = os.path.join("PyPoll", "analysis", "analysis_result.txt")

with open(output_path, "w") as file:
    file.write(f'''Election Results
---------------------------------
Total Votes: {numbervotes:,}
---------------------------------
''')
    for candidate in candidates:
        candidate_votes = sum(1 for row in csv.reader(open(csvpath)) if row[2] == candidate)
        percentage = (candidate_votes / numbervotes) * 100
        file.write(f'''{candidate}: {percentage:.2f}% ({candidate_votes:,})
''')

        if percentage > winpercentage:
            winpercentage=percentage
            winner=candidate
    file.write('''---------------------------------
''')
    file.write(f'''Winner: {winner}
---------------------------------''')