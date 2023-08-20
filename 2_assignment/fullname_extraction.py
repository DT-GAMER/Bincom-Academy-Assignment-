#!/usr/bin/python3

# Open the file "fullname.txt" in read mode
with open("fullname.txt", "r") as file:
    # Read the content of the file and remove any leading/trailing whitespace
    full_name = file.read().strip()

# Split the full name into individual components
first_name, surname, last_name = full_name.split()

# Print the extracted components of the name
print("First Name:", first_name)
print("Surname:", surname)
print("Last Name:", last_name)

