#!/usr/bin/env python3
import sys
from collections import defaultdict

current_boro = None
current_crime_count = 0
boro = None
crime_types = defaultdict(set)
boro_crime_counts = defaultdict(int)

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    boro, crime = line.split('\t', 1)
    
    if current_boro == boro:
        current_crime_count += 1
        crime_types[boro].add(crime)
    else:
        if current_boro:
            boro_crime_counts[current_boro] = current_crime_count
        current_boro = boro
        current_crime_count = 1
        crime_types[boro].add(crime)

# Output the last boro if needed
if current_boro == boro:
    boro_crime_counts[current_boro] = current_crime_count

# Find the borough with the most crimes
most_crime_boro = max(boro_crime_counts, key=boro_crime_counts.get)
most_crime_count = boro_crime_counts[most_crime_boro]
most_crime_types = crime_types[most_crime_boro]

print(f"Most of the crimes were reported in {most_crime_boro}")
print(f"Total number of crimes reported in {most_crime_boro} is {most_crime_count}")
print(f"Crime types reported in {most_crime_boro} are {', '.join(most_crime_types)}")

