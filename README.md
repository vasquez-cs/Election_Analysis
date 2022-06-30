# Congressional Election Analysis

## Overview of Election Audit: 

I am tasked with assisting Seth and Tom in completing the congressional election audit. I will assist by fufilling the election commission's request for additional audit data. The additional results being requested are:

* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

## Congressional Election-Audit Results: 

<img src="https://user-images.githubusercontent.com/107224632/176580409-bac76c9e-17d4-4e41-b8d6-8d6211666b30.png" width=40% height=40%><br />
*Figure 1: Final election_results.txt output*<br />

The election audit results give insight into which of the three counties voters participated from.

* There were a total of 369,711 votes cast in this congressional election
* Denver was the county with the largest number of votes cast
    * 306,055 county votes
    * Contributed 82.8% of the total votes cast
* Jefferson had in second largest number of votes cast 
    * 38,855 county votes 
    * Contributed 10.5% of the total votes cast
* Arapahoe had the least votes of the three counties
    * 24,801 county votes 
    * Contributed 6.7% of the total votes cast
   
In addtion to the county results, there was plenty to be analyzed for the three candidates in the congressional election race.

* Diana DeGette won the congressional election in a landslide victory
    * Vote count of 272,892
    * 73.8% of the total votes cast
* Candidate Charles Casper Stockham came in second place
    * Vote count of 85,213
    * 23.0% of the total votes cast
* Candidate Raymon Anthony Doane came in last place
    * Vote count of 11,606
    * 3.1% of the total votes cast
    
### Congressional Election-Audit Summary: 

This script has proven to handle a decently sized election results .csv file at 369,712 rows and be able to produce valid audit data for congressional election results and voter turnout. With some minor modifications, the script can be used to handle any other election. Two updates that can help this happen is to update the scripts that reads each row of the .csv file and to update the file output. 

<img src="https://user-images.githubusercontent.com/107224632/176605002-19db765a-b5af-4d5d-9765-7e1005b6c519.png" width=40% height=40%><br />
*Figure 2: election_results.csv file*<br />

<img src="https://user-images.githubusercontent.com/107224632/176608618-d621ec56-8388-447b-821f-0028ef6de6cf.png" width=60% height=60%><br />
*Figure 3: Section of PyPoll_Challenge.py script that scans the .csv file rows*<br />

As shown in figure 2 and 3, the script is build to handle a .csv file with three columns. For this script to be applied to any election, it is cruicial to review the .csv file that will be used. Assuming that the .csv to be used has a similar column/row structure as the current election_results.csv, we would first need to identify the "candidate" and "county" column or their equivelents. Once it is identified, if the index postion is different to what is in figure 2, then it will be updated accordingly. For example, if our new csv data had the candidate names in the 6th column instead of the current file's 3rd, line 56 of our PyPoll_Challenge.py script would be updated to "candidate_name = row[5]". This would be done so the script can pull the candidadte name from the the 5th index position of the new csv file.

The voter turnout portion of the script will still be valid. We would need to verify the voter turnout index position in the new .csv file and update it if needed, as we did in the example above. Even if the column we use for voter turnout contains different data such as state, country or numbered municipalities, our "county" related variables are still valid in the script. They are stlil valid because the variables holding the voter turnout names are appropriately named and read in the csv rows as string data. Finally there are sufficient comments to idenify which blocks of code are for the voter turnout and what actions are beinng performed. This allows any programmer in the to see the original programmmer's intention and purpose for each black of code.

<img src="https://user-images.githubusercontent.com/107224632/176611687-1e1ee553-72ec-4244-82c1-363169601cbf.png" width=85% height=85%><br />
*Figure 4: Section of current PyPoll_Challenge.py script that outputs the largest county name*<br />

Secondly, depending on what this script would be used for, our output would most likely to need some tweaking. One example of output script that may need updating can be seen in figure 3. Currently the script would output "Largest County Turnout" and then the county_name or equivilent value would print to the terminal window and later on to the election_results.txt output. If we apply the current script to a presidential election that wants to analyze voter turnout in the 50 states, our current preprogrammed text output wouldn't make much sense. The programmed message would need to be updated accordingly to accomodate the data being read for voter turnout. The required tweak could be as simple as changeing the script line 179 to " f"Largest State Turnout: {largest_county}\n" ". The outputted message would then make sense for the election commitee.
