import re

# Sample data string containing numbers and letters
data = "15267a98434 76 5"

# Regex pattern to match a digit (\d) repeated between 2 and 5 times
pattern = r"\d{2,5}"

# Regex pattern to match a digit (\d) repeated 2 or more times (no upper limit)
pattern = r"\d{2,}"

# Regex pattern to match a digit (\d) repeated up to 5 times (0 to 5 times)
pattern = r"\d{,5}"

# Find all substrings in 'data' that match the current 'pattern'
print(re.findall(pattern, data))