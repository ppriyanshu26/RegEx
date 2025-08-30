import re

# The text to search in for the first regex example
text = r"Hello, my_phone number is 123$%."

# Regex pattern explanation:
# 123      - matches the characters '123'
# \$       - matches a literal dollar sign '$'
# \%       - matches a literal percent sign '%'
# \.       - matches a literal dot '.'
# \Z       - asserts position at the absolute end of the string
pattern = r'123\$\%\.\Z'

# Find all matches of the pattern in the text
match = re.finditer(pattern, text)

# Iterate over all matches and print their start index and matched text
for i in match:
    print(i.start(), "-->", i.group())

# Second example: find all dates in the format YYYY-MM-DD in the text
text = "I have a meeting scheduled on 2025-09-01, shift it to 2025-09-02."

# Compile a regex pattern to match dates in the format YYYY-MM-DD
pat = re.compile(r'\d{4}-\d{2}-\d{2}')

# Find all matches of the date pattern in the text
match = re.finditer(pat, text)

# Iterate over all matches and print their start index and matched text
print("DATE:")
for i in match:
    print(i.start(), "-->", i.group())