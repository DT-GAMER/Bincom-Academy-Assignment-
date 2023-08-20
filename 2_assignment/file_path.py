#!/usr/bin/python3

# Import the 'os' module to interact with the operating system
import os

# Get the current working directory (the directory from which the script is being executed)
current_directory = os.getcwd()

# Print a descriptive message along with the current working directory
print("Current Directory:", current_directory)

# Construct the full file path by joining the current directory with the filename "fullname.txt"
file_path = os.path.join(current_directory, "file_path.py")

# Print a descriptive message along with the full file path
print("File Path:", file_path)

