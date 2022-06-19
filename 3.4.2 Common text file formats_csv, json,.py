import csv
from collections import Counter

with open(r'C:\Users\nikkr\Downloads\Crimes.csv') as f:
    crimes = [(row['Primary Type']) for row in csv.DictReader(f) if '2015' in row['Date']]
    print(Counter(crimes).most_common()[0][0])




