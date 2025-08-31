import re

# IGNORECASE
# data = "I love python. Python is awesome!"
# pattern = r"\bpython\b"
# matches = re.findall(pattern, data, re.IGNORECASE) # re.I
# print(matches)

# MULTILINE
# data = '''ppriyanshu 123
# 0pikachu 486
# pika789'''
# pattern = r"\d{3}$"
# matches = re.findall(pattern,data, re.MULTILINE) # re.M
# print(matches)

# DOTALL
# data = "hello\nworld"
# pattern = r"."
# matches = re.findall(pattern,data, re.DOTALL) # re.S
# print(matches)

# VERBOSE
# data = "hello.world"
# pattern = r"\w+(?#comment in between)\.\w+#comment at last"
# matches = re.findall(pattern,data, re.VERBOSE) # re.X
# print(matches)

# ASCII
data = "Hello 123 World, non-ASCII characters like Ç or ê should be ignored"
pattern = r"\b\w+\b"
matches = re.findall(pattern,data, re.ASCII) # re.A
print(matches)