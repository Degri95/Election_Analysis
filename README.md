# Election_Analysis
Using Python to analyze Colorado election results

## Overview of the Election Audit

In this project we are audititing election results of US congressional precinct in Colorado. We were given this task by an employee of the Colorado Board of Elections. We were provided a CSV file of the results to audit, and we exported our data in to a TXT file to present. Python and VS Code were the tools we used to perform our audit and analysis.

## Election Audiit Results

Using a Python script to analyze the data, we were able to provide the following results.

-Total number of votes cast: 369,711

-Number of votes and percentage of the votes for each county:
    -Jefferson: 10.5% (38,855)
    -Denver: 82.8% (306,055)
    -Arapahoe: 6.7% (24,801)

-Which County had the largest number of votes: Denver

-Number of votes and percentage of the total votes each cantidate received:
    -Charles Casper Stockham: 23.0% (85,213)
    -Diana DeGette: 73.8% (272,892)
    -Raymon Anthony Doane: 3.1% (11,606)

-Final results of the Election:
    -Winner: Diana DeGette
    -Winning Vote Count: 272,892
    -Winning Percentage: 73.8%


We were able to export all of this information into a text file with our script.
![Election Results](/Resources/Output.PNG)


## Election-Audit Summary

The script that we made successfully extracted and formatted the election resulsts. It's possible to use this script to analyze any other past or future election results with some modifications. 
We could scale the election size up and gather information by State if our data had the information. We could also add variables to gather information by city if the information was provided. By using similar code to what was used to gather the information for the election and county votes we could add almost any other attribute.