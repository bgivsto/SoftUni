import re

pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"

links = []
while True:
    line = input()
    if not line:
        break

    matches = re.finditer(pattern, line)
    for match in matches:
        data = match.group()
        links.append(data)

for link in links:
    print(link)