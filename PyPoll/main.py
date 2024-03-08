import os
import csv

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

numbervotes = 0
candidates = {}
winner = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        numbervotes += 1
        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

winpercentage = 0
winner = ""

print(f'''Election Results
---------------------------------
Total Votes: {numbervotes:,}
---------------------------------''')

for candidate, votes in candidates.items():
    percentage = (votes / numbervotes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})")

    if percentage > winpercentage:
        winpercentage = percentage
        winner = candidate

print('---------------------------------')
print(f'Winner: {winner}')
print('---------------------------------')


output_path = os.path.join("PyPoll", "analysis", "analysis_result.txt")


with open(output_path, "w") as file:
    file.write(f'''Election Results
               
---------------------------------
               
Total Votes: {numbervotes:,}

---------------------------------
''')

    for candidate, votes in candidates.items():
        percentage = (votes / numbervotes) * 100
        file.write(f'''
{candidate}: {percentage:.2f}% ({votes})
''')

    if percentage > winpercentage:
        winpercentage = percentage
        winner = candidate

    file.write('''
---------------------------------''')
    file.write(f'''

Winner: {winner}

''')
    file.write('---------------------------------')