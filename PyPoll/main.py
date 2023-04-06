import os
import csv

csvpath = os.path.join("Resources", "election_data")

with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile)

    total = 0
    can_list = []
    can_votes = {}

    next(csvreader)

    for row in csvreader:
        can_name = row[2]
        total +=1

        if can_name not in can_list:
            can_list.append(can_name)
            can_votes[can_name] = 0
            can_votes[can_name] +=1

            

        



        









output = f'''

Election Results
-------------------------
Total Votes: {total}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''
print(output)