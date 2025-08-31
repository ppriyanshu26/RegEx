import re

email = input("Enter email: ")
pat = r"^[a-zA-z][\w+\.]+@\w+\.\w+"

match = re.match(pat, email, re.I)
if match:
    print("Valid email")
else:
    print("Invalid email")
