#!/usr/bin/env python3
import sys

current_month = None
current_count = 0
month = None

number2english = {
    1: 'January',
    2: 'Febuary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t')
    count = int(count)

    if current_month == month:
        current_count += count
    else:
        if current_month:
            # Output the count for the previous month
            print(f"{number2english[int(current_month)]} {current_count}")
        current_count = count
        current_month = month

if current_month == month:
    print(f"{number2english[int(current_month)]} {current_count}")

