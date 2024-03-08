import os
import csv

csvpath = os.path.join('Pybank','Resources', 'budget_data.csv')

months= 0
total = 0
previous_profitloss=0
changes=[]
total_changes=0
previous_profit=None
max_amount=0
max_date=""
min_amount=0
min_date=""




with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next (csvreader)
    for row in csvreader:
        months+=1
        total+= int(row[1])
        profit_change=int(row[1])
        date=row[0]
        profit=int(row[1])

        if previous_profitloss != 0:
            change = profit_change - previous_profitloss
            changes.append(change)
            total_changes += change
        previous_profitloss = profit_change

        if previous_profit is not None:
            profitdifference= profit-previous_profit
            if profitdifference > max_amount:
                max_amount= profitdifference
                max_date=date
            if profitdifference<min_amount:
                min_amount=profitdifference
                min_date=date

        previous_profit=profit


average_change=total_changes/(months-1)

print(f'''Financial Analysis
-------------------------------------
Total months: {months}
Total: ${total}
Average change: ${average_change:.2f}
Greatest increase in profits: {max_date}: (${max_amount:.2f})
Greatest decrease in profits: {min_date}: (${min_amount:.2f})''')

output_path = os.path.join("PyBank", "analysis", "analysis_result.txt")


with open(output_path, "w") as file:
    file.write(f'''Financial Analysis
-------------------------------------
Total months: {months}
Total: ${total}
Average change: ${average_change:.2f}
Greatest increase in profits: {max_date}: (${max_amount:.2f})
Greatest decrease in profits: {min_date}: (${min_amount:.2f})''')