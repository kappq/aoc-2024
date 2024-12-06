import re

with open("input.txt") as f:
    memory = f.read()

total = 0

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)
