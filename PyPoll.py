# The data we need to retrieve

#import csv
#import os

##Assign a variable for the file to load and the path.
#file_to_load = os.path.join("..","Resources","election_results.csv")

## Open the election results

#with open(file_to_load) as election_data:

##To do: Perform analysis
    #print(election_data)

##Close the file


# 1. The total number of votes cast
# 2. A complete list of canidate who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote






#file_to_load="Resources/election_results.csv"

#with open(file_to_load) as election_data:
    #print(election_data)

import os
file_to_load = os.path.join("..", "Resources", "election_results.csv")
with open(file_to_load, "r", encoding="utf-8") as election_data:
    print(election_data)