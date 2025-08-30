import re

# Compile pattern to match 'ab', case-insensitive
pattern = re.compile(r"ab", re.IGNORECASE)
data = "abaababa"

# Find all non-overlapping matches as an iterator
match_iter = re.finditer(pattern, data)

print(match_iter)  # Print the iterator object
print(type(match_iter))  # Print the type of the iterator

# Iterate through all matches and print details
for i in match_iter:
    print(f"\nElement: {i.group()} with Start: {i.start()} and End: {i.end()}\n{i}\n")

# Find all matches and return them as a list
match_list = re.findall(pattern, data)

print(match_list)  # Print the list of matches
print(type(match_list))  # Print the type of the list

# Compile pattern to match 'dog' or 'cat'
pattern = re.compile(r'dog|cat')
data = "I saw Dog running behind the cat and then cat climbed but dog couldn't"

# Find all matches of 'dog' or 'cat' as an iterator
match_iter = re.finditer(pattern, data)

# Print each match object
for i in match_iter:
    print(i)