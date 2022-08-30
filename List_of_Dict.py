    #Creating a list of Dictionaries
voting_data = []
    # once created, we want to add or append the dict.
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
    # print(voting-data)
    # How many votes did you get
my_votes = int(input("How many votes did you get in the election?"))
    # Total votes in the election
total_votes = int(input("What is the total votes in the election?"))
    # Calculate the percentage of votes you recieved
percentage_votes = (my_votes / total_votes) * 100
print("I recieved" + str(percentage_votes)+"% of the total votes.")
