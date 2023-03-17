import re

text = input()
pattern = r"(?<=[\s]_)[a-zA-Z]+\b"
match = re.findall(pattern, text)
print(*match, sep=",")
