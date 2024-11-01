import os
# Open the file 'chinu.txt' in write mode
f = open("chinu.txt", "w")

# Write the first string "CHinu" to the file
f.write("CHinu")

# Write the second string " CHinmaya" to the file
f.write(" CHinmaya")

# Close the file to ensure all data is written and resources are released
f.close()

# Open the file 'chinu.txt' in read mode to read the content
f = open("chinu.txt", "r")

# Read the entire content of the file into a variable 'content'
content = f.read()
# Print the content read from the file
print("Content of the file:", content)

# Move the file pointer back to the beginning of the file
f.seek(0)

# Read a single line from the file and store it in 'line'
line = f.readline()
# Print the first line read from the file
print("First line:", line)

# Move the file pointer back to the beginning of the file again
f.seek(0)

# Read all lines from the file into a list 'lines'
lines = f.readlines()
# Print the list of all lines read from the file
print("All lines:", lines)

# Get the current position of the file pointer and store it in 'position'
position = f.tell()
# Print the current position in the file
print("Current position in the file:", position)

# Open the file in read/write mode (r+) to truncate it
f = open("chinu.txt", "r+")
# Truncate the file to the first 5 characters (cut off the rest)
f.truncate(5)

# Close the file again
f.close()

# Open the file again in read mode to check the content after truncation
f = open("chinu.txt", "r")

# Read the new content of the file after truncation into 'new_content'
new_content = f.read()
# Print the content of the file after truncation
print("Content after truncation:", new_content)

# Close the file
f.close()
