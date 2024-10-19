from csv import reader
from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext(appName="hw2")
sc.setLogLevel("ERROR")

# Read input data from HDFS
data = sc.textFile("hdfs://group11-1:54310/hw1-input/")

# Use csv.reader to split CSV rows correctly
splitdata = data.mapPartitions(lambda x: reader(x))

# Filter rows where the crime type (column index 7) is not blank
valid_data = splitdata.filter(lambda x: x[7]) # Ensuring sufficient columns

### Question A: Where is most of the crime happening?
location_crime_count = valid_data.map(lambda x: (x[13], 1)).reduceByKey(lambda a, b: a + b)
# Get the location with the most crimes
most_crime_location = location_crime_count.sortBy(lambda x: -x[1]).take(1)
print "Location with most crimes: {}, Total crimes: {}".format(most_crime_location[0][0], most_crime_location[0][1])

### Question B: What are the top 3 crimes in July?
# Filter rows to keep only July data
july_data = valid_data.filter(lambda x: x[5].split("/")[0] == "07")

# Map to (OFNS_DESC, 1), then reduce by key (offense description)
july_crime_count = july_data.map(lambda x: (x[7], 1)).reduceByKey(lambda a, b: a + b)
# Get the top 3 crimes in July by count
top_3_july_crimes = july_crime_count.sortBy(lambda x: -x[1]).take(3)
print "Top 3 crimes in July:"
for crime, count in top_3_july_crimes:
    print "{}: {} crimes".format(crime, count)

### Question C: How many DANGEROUS WEAPONS crimes were reported in July?
# Filter for 'DANGEROUS WEAPONS' crimes in July
dangerous_weapons_july = july_data.filter(lambda x: x[7] == 'DANGEROUS WEAPONS')

# Count the number of such crimes
dangerous_weapons_count = dangerous_weapons_july.count()
print "Number of DANGEROUS WEAPONS crimes in July: {}".format(dangerous_weapons_count)

