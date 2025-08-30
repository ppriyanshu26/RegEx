
# Import the regular expressions module
import re


# Compile the pattern for case-insensitive matching
pattern = re.compile(r"Python", re.IGNORECASE)
# The data string to match against
data = "python programming"
print(type(pattern))  # Print the type of the compiled pattern


# Try to match the pattern at the start of the string
match = re.match(pattern, data)
print(match)  # Print the match object
print(type(match))  # Print the type of the match object


# Check if a match was found
if match:
    print("Match found:", match.group())  # Print the matched text
else:
    print("No match found")  # Print if no match is found
