import re

data = "(555)+91-907,576,3738  (7753)978,965,7845  (123) +92-907,865,4367"
pattern = r'\(\d{3,4}\)\s?(?:\+\d{2}-)?\d{3},\d{3},\d{4}'
matches = re.findall(pattern, data)
print(matches)