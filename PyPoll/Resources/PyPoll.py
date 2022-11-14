#PyPoll Homework: Module 3 Python                                  November 14, 2022

#Add dependencies.
import csv
import os

#Add variables to load a file from a path.
file_to_load = os.path.join("Resources", "election_data.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize vote counter 
total_votes = 0 

#Candidate options and votes 
candidate_options = []
candidate_votes = {}

#Winning candidate, vote count, and %
winning_candidate = ""
winning_count = 0 
winning_percent = 0 

#Read the csv file and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1 
        candidate_name = row[2]
        county_name = row[1]

        #conditionals for count - if candidate does not match existing names add it to the list

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1 

#Save txt file
with open (file_to_save, "w") as txt_file:

    #Print vote count 
    election_data = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n\n")
    print (election_data, end = "")
    
    txt_file.write (election_data)
    
    #For loop for candidate vote count 
    for candidate_name in candidate_votes: 
        votes = candidate_votes.get(candidate_name)
        vote_percent = float(votes) / float (total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
        
        print (candidate_results)
        txt_file.write (candidate_results)

        #determine winning candidate 
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

 

    


