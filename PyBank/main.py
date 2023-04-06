# modules
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
my_report = open('Analysis/Budget_Report.txt', 'w')

# # Open the CSV
with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile)

    total = 0
    months = 0
    pre_rev = 0
    total_ch = 0
    inc = ['',0]
    dec = ['',0]

    next(csvreader)
    # Loop through looking for values
    for row in csvreader:
        rev = int(row[1])

        total += rev
        months += 1

        change = rev - pre_rev

        if(pre_rev == 0):
            change = 0
        
        total_ch += change
        pre_rev = rev

        if(change>inc[1]):
            inc[0] = row[0]
            inc[1] = change

        if(change<dec[1]):
            dec[0] = row[0]
            dec[1] = change

       
output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)