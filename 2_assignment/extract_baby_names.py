#!/usr/bin/python3

# Import the 're' module for regular expressions
import re

# Read the content of the HTML file and store it in 'html_content'
with open("baby_names.html", "r") as file:
    html_content = file.read()

# Define a regular expression pattern to extract baby names
pattern = r"Baby names: ([\w, ]+)"

# Define a function to perform custom findall using regex without built-in libraries
def findall(pattern, text):
    # Create an empty list to store the matched substrings
    matches = []
    
    # Initialize the starting point for searching in the text
    start = 0
    
    # Loop until no more matches are found
    while True:
        # Search for a match using the provided pattern starting from 'start'
        match = re.search(pattern, text[start:])
        
        # If no more matches are found, exit the loop
        if not match:
            break
        
        # Append the matched substring to the 'matches' list
        matches.append(match.group(1))
        
        # Update the starting point for the next search
        start += match.end()
    
    # Return the list of matched substrings
    return matches

# Find all matches of the pattern in the HTML content using the custom_findall function
matches = findall(pattern, html_content)

# Check if any matches were found
if matches:
    # Split the first match into individual baby names using comma and space
    baby_names = matches[0].split(", ")
    print("Extracted Baby Names:", baby_names)
else:
    print("No baby names found in the HTML content.")

