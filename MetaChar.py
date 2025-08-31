import re

# Example regex patterns and data 
# data = "hello world i am priyanshu priyam hee hee hehehe"
# pattern = r"(he)+"

# data = "my email address are example@example.com and test2@test.com"
# pattern = r"\w+@\w+\.\w+"

# data = "abb ac aaabbb aaa aaabbcc bb"
# pattern = r"a*b+[A-Z]*"

# data = "4hello world"
# pattern = r"^\d"

# data = '''hello world6 
# yokoso7'''
# pattern = r"\d$"

# data = "call me on 123-456-7890 or 1234567890"
# pattern = r"\d{3}-?\d{3}-?\d{4}"

# match = re.finditer(pattern, data, re.MULTILINE)
# for i in match:
#     print(i.start(),"-->",i.group())

# List of URLs to test the regex pattern
urls = ['http://Example1.com','https://www.example.org','htttps://file.net']

# Regex pattern to match URLs starting with http or https, optional 'www.', followed by domain name and TLD
pattern = r"https?://(www\.)?\w+\.\w+"

# Iterate through each URL in the list
for i in urls:
    # If the URL matches the pattern, print it
    if re.match(pattern,i):
        print(i)
