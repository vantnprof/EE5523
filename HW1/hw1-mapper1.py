#!/usr/bin/env python3
from csv import reader
import sys


for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime or boro == "BORO_NM":
        continue
    print(f"{boro}\t{crime}")
