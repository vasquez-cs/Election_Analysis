# Congressional Election Analysis

## Overview of Election Audit: 

I am tasked with assisting Seth and Tom in completing the congressional election audit. I will assist by fulfilling the election commission's request for additional audit data. The additional results being requested are:

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
* Jefferson had the 2<sup>nd</sup> largest number of votes cast 
    * 38,855 county votes 
    * Contributed 10.5% of the total votes cast
* Arapahoe had the least votes of the three counties
    * 24,801 county votes 
    * Contributed 6.7% of the total votes cast
   
In addition to the county results, there was plenty to be analyzed for the three candidates in the congressional election race.

* Diana DeGette won the congressional election in a landslide victory
    * Vote count of 272,892
    * 73.8% of the total votes cast
* Candidate Charles Casper Stockham came in 2<sup>nd</sup> place
    * Vote count of 85,213
    * 23.0% of the total votes cast
* Candidate Raymon Anthony Doane came in last place
    * Vote count of 11,606
    * 3.1% of the total votes cast
    
### Congressional Election-Audit Summary: 

This script has proven to handle a decently sized election result comma seperated value (csv) file with 369,712 rows. In addition the script has produced valid audit data for congressional election results and voter turnout. With some minor modifications, the script can be used to handle any other election. Two updates that can make this possible are to update the scripts that read each row of the csv file and to update the file output. 

<img src="https://user-images.githubusercontent.com/107224632/176605002-19db765a-b5af-4d5d-9765-7e1005b6c519.png" width=40% height=40%><br />
*Figure 2: election_results.csv file*<br />

<img src="https://user-images.githubusercontent.com/107224632/176608618-d621ec56-8388-447b-821f-0028ef6de6cf.png" width=60% height=60%><br />
*Figure 3: Section of PyPoll_Challenge.py script that scans the .csv file rows*<br />

As shown in figures 2 and 3, the script is built to handle a csv file with three columns. For this script to be applied to any election, it is crucial to review the csv file that will be used. Assuming that the csv to be used has a similar column/row structure as the current election_results.csv, we would first need to identify the "candidate" and "county" or its equivalent column. Once it is identified, if the index position is different from what is in figure 2, the script will be updated accordingly. For example, if our new csv data file has the candidate names in the 6<sup>th</sup> column instead of the current file's 3<sup>rd</sup>, line 56 of our PyPoll_Challenge.py script would be updated to "candidate_name = row[5]". This would be done so the script can pull the candidate name from the 5<sup>th</sup> index position of the new csv file.

The majority of the voter turnout scripts and code blocks will still be valid. As with the candidate name above, the programmer would need to verify the voter turnout index position in the new csv file and update it if necessary. Even if the column we use for voter turnout contains different data such as state, country, or zip codes, our "county" related variables are still valid in the script. They are valid because the voter turnout-related variables are appropriately named and will read in the csv rows as string data. Finally, there are sufficient comments to identify which blocks of code are for voter turnout and what actions are being performed. This allows the programmer to review the intention and purpose for each block of code related to voter turnout and make more tweaks if needed.

<img src="https://user-images.githubusercontent.com/107224632/176611687-1e1ee553-72ec-4244-82c1-363169601cbf.png" width=85% height=85%><br />
*Figure 4: Section of current PyPoll_Challenge.py script that outputs the largest county name*<br />

Secondly, depending on what type of election this script would be used for, our final output to both the terminal window and the text file would most likely require tweaking. One example of the output script requiring an update can be seen in figure 3. Currently, the script would output the "Largest County Turnout" text with the county_name value to the terminal window and the election_results.txt file. While the variable name isn't important as the expected value will output, the prepopulated text would be confusing if the election turnout is not for counties. For example, if we apply the current script to a presidential election that wants to analyze voter turnout in the 50 states, our current preprogrammed text on line 179 would confuse the reader if they only received the text file to review. For this scenario, a simple modification can prevent confusion. The modification would be to update line 179 to: " f"Largest State Turnout: {largest_county}\n" ". The slight change will make the output comprehensible to the election committee or who else reviews the terminal window or final output text file. 

The current election analysis script is a good foundation to be used in any election. Even if the scope increases, the script skeleton could be refactored to handle different input files, improve run time or even perform even more detailed calculations.
