# h1b_analysis
h1b analysis for insight
Python version: 3.5
Using CSV package from python standard library, this program reads provided H1b data line by line, and check if the data entry is CERTIFIED.
For CERTIFIED cases, it will maintain a counter for job title based on SOC-CODE, and the employee work location (state).
After counting all the data entry, it will output the top_10 occupation and state into corresponding txt files.

Time complexity: O(n)-- it's reading data line by line, and access each item by calling its index

Testing:  passed provided testing script

test
