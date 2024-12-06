import re

with open("input.txt") as f:
    memory = f.read()

total = 0
do = True

matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\)|don\'t\(\))", memory)
for match in matches:
    if match[3] == "do()":
        do = True
    elif match[3] == "don't()":
        do = False

    if do and match[1] and match[2]:
        total += int(match[1]) * int(match[2])

print(total)
