import csv
import os
from unicodedata import name


file_to_load = os.path.join("Resources", "PyPoll_Challenge.csv")
file_to_save = os.path.join("Results", "election_analysis.txt")

total_votes = 0


candidate_options = []
candidate_votes = {}

county_options = [] 
county_votes = {}


winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""

winning_county_votes = 0
winning_county_votes_percentage = 0


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    headers = next(reader)
 
    for row in reader:
       total_votes = total_votes + 1
    
       candidate_name = row[2]

       county_name = row[1]

    if candidate_name not in candidate_options:

        candidate_options.append(candidate_name)

        candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] +=1

    if county_name not in county_options:

        county_options.append(county_name)

        county_votes[county_name] = 0

        county_votes[county_name] +=1     

with open(file_to_save, 'w') as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n") 
    print(election_results, end="")

    txt_file.write(election_results)

    for county_name in county_votes:

        c_votes = county_votes[county_name]
        c_votes_percentage = float(c_votes) / float(total_votes) *100

        county_results = (f"{county_name}: {c_votes_percentage:.1f}% ({c_votes:,})\n")

        print(county_results)

        txt_file.write(county_results)

        if(c_votes > winning_county_votes):
            winning_county_votes = c_votes
            winning_county = county_name
            winning_county_votes_percentage = c_votes_percentage

    winning_county_summary = (
        f"------------------------\n"
        f"County with the highest turnout: {winning_county}\n"
        f"Vote Count for {winning_county}: {winning_county_votes:,}\n"
        f"Percentage of total votes for {winning_county}: {winning_county_votes_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_county_summary)

    txt_file.write(winning_county_summary)

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):        
           
            winning_count = votes
            winning_candidate = candidate_name 
            winning_percentage = vote_percentage
            
            # Print wimming candidates votes to terminal
                         
        winning_candidate_summary = (
            f'----------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'----------------\n')  

        print(winning_candidate_summary) 

       
        txt_file.write(winning_candidate_summary)

