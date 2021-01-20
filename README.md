# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Diana DeGette
  - Raymon Anthony Doane
  - Charles Casper Stockham
- The candidate results were:
  - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
  - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
  - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
- The winner of the election was:
  - Diana DeGette, who received "73.8%" of the vote and "272,892" number of votes.
  
## Challenge Overview

## Project Overview
The election commission has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.

## Resources
- Data source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Challenge Results

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Diana DeGette
  - Raymon Anthony Doane
  - Charles Casper Stockham
- The candidate results were:
  - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
  - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
  - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
- The winner of the election was:
  - Diana DeGette, who received "73.8%" of the vote and "272,892" number of votes.
- The county vote results were:
  - Jefferson county had "10.5%" of the votes coming to a value of "38,855" votes.
  - Denver county had "82.8%" of the votes coming to a value of "306,055" votes.
  - Arapahoe county had "6.7%" of the votes coming to a value of "24,801" votes.
- The largest county turnout was:
  - Denver county, which accounted for "82.8%" of the votes at a total of "306,055" votes.
  
## Challenge Summary

 This code can be used for any election. Small changes may be necessary, but would allow for any election voting results to be summarized in a much quicker than doing it through excel or manually. The two main areas of the script that would need to be changed are the following:
 - 1) "Line9: file_to_load = os.path.join("Resources", "election_results.csv")
   - The above code represents the path that the script is pulling data from. In this case, it is pulling the file named "election_results.csv" from my "Resources" folder. These two parts may need to be renamed depending on what the file pathway is to the data you are trying to pull and what the file is called.
 - 2) "Line11: file_to_save = os.path.join("analysis", "election_results.txt")
  - Similar to the above situation, this text describes where the output of our data will go. So depending on where you want the text file to end up and what you want the text file to be named, you will have to edit those two areas as well. 
