
# Import the regular expressions module
import re


# Define the pattern to search for
pattern = r"Python"
print(type(pattern))  # Print the type of the pattern
print(pattern)  # Print the pattern

# The data string to search in
data = "I love python programming"


# Search for the pattern in data (case-insensitive)
match = re.search(pattern, data, re.IGNORECASE)
print(match)  # Print the match object


# Check if a match was found
if match:
    print("Match found:", match.group())  # Print the matched text
else:
    print("No match found")  # Print if no match is found
