#!/usr/bin/env python3
import sys
import csv

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    reader = csv.reader([line])
    for row in reader:
        # Assuming the CSV columns are: Date, CrimeType, Location, etc.
        date, crime_type = row[1], row[7]
        if crime_type == "DANGEROUS WEAPONS":
            month = date.split('/')[0]  # Extract month from date
            print(f"{month}\t1")

