import re

text = "     This  is   a sentence with   extra spaces .  "
pattern = r'\s+'
cleaned_text = re.sub(pattern, " ", text).strip()
cleaned_text = re.sub(r'\s+([?.!,])', r'\1', cleaned_text)
print(cleaned_text)