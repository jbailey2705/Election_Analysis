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
#print("The time right now is ", now)


import csv
import os
dir(csv)

#file_to_load = os.path.join("..", "Resources", "election_results.csv").replace("/","\")

file_to_load = "Resources/election_results.csv"
election_data = open(file_to_load, "r")

with open (file_to_load) as election_file:
    election_data = csv.reader(election_file)
    

 # Prints the file to open   
    #print(election_data)

# Will look in the rows of the file
    for row in election_data:

# Prints the Rows in the file
        #print (row)

        import csv
        import os

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load)as election_data:

    ####print(election_data)

 # Using the open() function with the 'w' mode we will write data to the file
 # open(file_to_save, "w")

    file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")


# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Close the file
# outfile.close

# Write 3 countries to the txt file on seperate lines using \n, this will break up the text in the file

    txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")


import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    for row in file_reader:
        ####print(row)


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

# Adding out Dependencies.

        import csv
        import os

# Assigning a variable to load & save a file path.

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis")

# Initialize a total vote counter

total_votes = 0

# Candidate options.

candidate_options = []

# Open the election results & read the file

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
 
 # Read the Header Roe
 
    headers = next(file_reader)
 
 # Print each row in the CSV file

    for row in file_reader:

        # Add to the total vote count

        total_votes += 1 

# Print the candidate name to the candidate list & '.append' the list

candidate_name = row[2]

# If candidate does not match any existing candidate...

if candidate_name not in candidate_options:

    # Add it to the list of candidates

    candidate_options.append('candidate_name')

# Print the candidtate list

##### print(candidate_options)


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate & Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

     # Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

           # 3. Add a vote to that candidates count
        candidate_votes[candidate_name] +=1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:

    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

            # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     
        # 2. If true then set winning_count = votes and winning_percent =  # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f'----------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'----------------\n')  

print(winning_candidate_summary) 





# Print the candidate vote dictionary.
#print(candidate_votes)
