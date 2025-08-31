import re

# data = "Email addresses: user@example.com, admin@domain.com, me@ppriyanshu26.online"
# pattern = r"(\w+)@(\w+)\.(\w+)"
# match = re.findall(pattern, data, re.IGNORECASE)
# for i in match:
#     print("Username:", i[0])
#     print("Domain:", i[1])
#     print("Type:", i[2])
#     print("--------------------------------")

# html = '''<a href = "https://www.instagram.com">Instagram</a>
# <a href = "https://www.telegram.com">Telegram</a>
# <a href = "https://www.discord.com">Discord</a>'''
# pattern = r'<a href = "([^"]+)">([^<]+)</a>'
# match = re.findall(pattern, html)

# for i in match:
#     print("Link:", i[0])
#     print("Text:", i[1])
#     print("--------------------------------")

# text = "incidents happened on 13/11/2023 12:23:24 and 11/10/2022 01:45:31"
# pattern = r"\d{2}/(\d{2})/(\d{4}) \d{2}:\d{2}:\d{2}"
# match = re.findall(pattern, text)
# for i in match:
#     print("Month:",i[0])
#     print("Year:", i[1])

text = "Visit https://www.example.com or http://example.com"
pattern = r"https?://(?:www\.)?\w+\.\w+"
matches = re.findall(pattern, text)

for i in matches:
    print(i)