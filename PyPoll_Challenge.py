# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""
"""By Carlos S. Vasquez"""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

    # initialize "county_list" as a list by use of []
county_list = []

    # initialize "county_votes" as a dictionary by use of {}
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.

    # initialize "largest_county" as empty string with empty quotation marks
largest_county = ""

    # Set "voter_turnout" to zero to hold the number of votes for the county with the largest turnout.
voter_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.

            # County name data to be pulled from the csv column "County". This column is identified by it's index position of '1' in the script
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.

            # Created a decision statement by using the previously created "county_name" variable and using
            # the logical operator "not" to find cases where the "county_name" didn't match 
            # existing values in the "county_list". 
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
               
                # If the "county_name" was not in "county_list" (decision statement is true), the value would get added 
                # to the "county_list" using the append() function
            county_list.append(county_name)
        
            # 4c: Begin tracking the county's vote count.

                # This script starts to track the vote count for each county
                # by populating the "county_votes" dictionary with both the key ("county_name") and 
                # the value (vote count). The script below sets the county's vote count to start at zero. 
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.

            # This script alters our "county_votes" dictionary on every loop where a row in the .csv is read.
            # This is done by adding '1' to the vote count that was started in the previous 4c script (started at zero)
            # when a corresponding "county_name" value is read in the .csv file.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # New decision statement created by using the previously created "county_votes" dictionary and 
        # the logical operator "IN" to find cases where the "county_name" matches 
        # existing names in the dictionary
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.

            # create "c_votes" variable to hold the individual vote count for each county in
            # the "county_votes" dictionary as it goes through the current for loop (for every county_name in "county_votes" dictionary)
        c_votes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.

            # Retooled the calculation used for candidate votes below.
            # Created "c_vote_percentage" variable to hold the value of the percentage calculation for each county as it goes through the 
            # current for loop (for every "county_name" in "county_votes"). Calculation performed has each county's "c_votes" value
            # ("county_name" vote count) divided by the "total_votes" variable, which represents the number of voters in the entire election. 
            # 
            # Also I created the "county_results" variable to hold the "county_name", "c_vote_percentage", 
            # "c_votes" as a single string value, enabling a simple text file save in step #6e. The "county_result" 
            # string is updated for every loop (every "county_name" in "county_votes" dictionary)
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
         # 6d: Print the county results to the terminal.

            # This script prints out the terminal message using the variables from "county_results".
            # This script was used instead of print(county_results) since it allowed me to remove the "\n"
            # and have the terminal output not have the spaces between the county lines after the 
            # "County Votes" line. This allowed me to match my terminal ouput to the terminal screenshot in the grading rubic. 
        print(f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})")

         # 6e: Save the county votes to a text file.

            # This script saves the "county_results" string created in #6c above to the text file "election_results.txt"
            # I had an easier time navigating the terminal output than the text file, so I only referenced "county results" here
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.

            # This decision statement determines which county has the highest number of votes. It uses the "c_votes" value for each county and 
            # compares it to the "voter_turnout" counter (starts at zero on the first loop; zero value was set in step #2)
            # As each "county_name" goes through the loop and the "c_votes" is larger than than the "voter_turnout" value, the "c_votes" value 
            # for that loop replaces the existing "voter_turnout" value. Once all the loops are done, the final stored value in the "voter_turnout" 
            # variable will be the largest value
        if c_votes > voter_turnout:
            voter_turnout = c_votes
            largest_county = county_name


    # 7: Print the county with the largest turnout to the terminal.
        
        # created "largest_county_summary" variable to hold the largest_county value and further ouput formatting as a string value, 
        # enabling a simple print statement to the terminal and to the text file print in step #8. The "largest_county_summary" string is updated 
        # once all the loops in the "for county_name in county_votes" script are done running.
    largest_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    
        # This script saves the "largest_county_summary" string created in #7 above to the text file "election_results.txt"
    txt_file.write(largest_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
