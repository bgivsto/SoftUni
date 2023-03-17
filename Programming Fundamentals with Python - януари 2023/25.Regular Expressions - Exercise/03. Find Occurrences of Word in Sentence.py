import re

text = input()
pattern = '\\b' + input() + '\\b'

match = re.findall(pattern, text, re.IGNORECASE)
print(len(match))