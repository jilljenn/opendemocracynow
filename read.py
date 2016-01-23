import csv
with open('votes.csv', newline='') as csvfile:
    votes = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for row in list(votes)[:5]:
        print(','.join(row))
