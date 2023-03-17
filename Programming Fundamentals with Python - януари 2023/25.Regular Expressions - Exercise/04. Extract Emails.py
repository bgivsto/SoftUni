import re

text = input()
pattern = r"\b[\w]+([\.\-]\w+)?@[a-zA-Z]+(([\.\-]\w+)+)?"
matches = re.finditer(pattern, text)

for match in matches:
    data = match.group()
    print(data)