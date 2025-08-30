import re

pattern = r'[^a-z 0-9.]'
data = "The price is $100.O"

# Find all matches of the pattern in the data
matches = re.finditer(pattern, data)

for i in matches:
    print(i)