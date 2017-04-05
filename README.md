# The VenD Challenge

You are Census Director of Quetta. Approximate population of Quetta is 1 million. There are 24 attributes to be collected for each person. Value of these attributes will either be Yes or No. Write a solution to store/retrieve the 24 attributes of each person in memory (RAM).

# Constraint:
- Cannot use byte type

# Solution has two performance metrics:
1. Memory required for the solution should be as minimum as possible. [Must not exceed: 6 Megabytes]
2. Retrieval time of any random single record should be as minimum as possible. Retrieval time complexity should be O(1).

# Interface:
- Two methods are to be exposed
    1. To store the data for people: This will read an array of arrays from a JSON input file provided and store data as per data structure of choice in memory.
    2. To retrieve the data for a single person: It will be based on index of that person as per the JSON input file.

# Expected Solution will contain:
1. Solution file
2. Maximum memory required for solution
3. Maximum Retrieval time of any random single record
4. Any means/code used to calculate the (2) and (3)

# Languages Allowed:
C, C++, C#, Java

# Provided Input File (generator.py):
Since the data file is large you can generate your own data file with the provided python script (generator.py)
You need to run the following command
python <path_to_generator.py>
This will take some time and generate another file (quetta.json) of around 150 Megabytes next to generator.py

quetta.json will be a JSON file which contains an array of arrays. Each array inside the main array represents single person's data therefore contains 24 string values either 'Yes' or 'No'.

# Submission:
For submission, email with the subject "The VenD Challenge" at murtaza.zaidi@venturedive.com
Post your questions below "The VenD Challenge" post at VentureDive's facebook page
