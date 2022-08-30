    # Open the data file "Election Results"
    # 1. The total number of votes cast
    # 2. A complete list of candidates who recieved votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election base on popular vote 
    # Import the datetime class from the datetime module.
from ast import increment_lineno
import datetime as dt
from email import header

from importlib import resources
from importlib.resources import Resource
from json import load
from re import I
from unittest import result
from wsgiref import headers
    # Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
    # Print the present time.
print("The time right now is ", now)


import csv
import os
dir(csv)

#file_to_load = os.path.join("..", "Resources", "election_results.csv").replace("/","\")

file_to_load = "Resources/election_results.csv"
election_data = open(file_to_load, "r")

with open (file_to_load) as election_file:
    election_data = csv.reader(election_file)
    

 # Prints the file to open   
    print(election_data)

# Will look in the rows of the file
    for row in election_data:

# Prints the Rows in the file
        print (row)

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load)as election_data:

    print(election_data)

 # Using the open() function with the 'w' mode we will write data to the file
 # open(file_to_save, "w")

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")


# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Close the file
#outfile.close

# Write 3 countries to the txt file on seperate lines using \n, this will break up the text in the file

    txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    for row in file_reader:
        print(row)


#### Skipping the Header Rows
#import csv
#import os

#file_to_load = os.path.join("Resources", "election_results.csv")
#file_to_save = os.path.join("analysis", "election_analysis.txt")

#with open(file_to_load) as election_data:
 #   file_reader = csv.reader(election_data)
#for headers in file_reader:
 #   headers = next(file_reader)
  #  print(headers)




