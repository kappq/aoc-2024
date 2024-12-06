def count_xmas(s):
    count = 0

    for i in range(len(s) - 3):
        word = s[i:i + 4]
        if word == "XMAS" or word == "SAMX":
            count += 1

    return count


with open("input.txt") as f:
    word_search = list(map(str.strip, f.readlines()))

width, height = len(word_search[0]), len(word_search)

count = 0

rows = [[] for _ in range(height)]
cols = [[] for _ in range(width)]
fdiags = [[] for _ in range(width + height - 1)]
bdiags = [[] for _ in range(len(fdiags))]

for i in range(height):
    for j in range(width):
        char = word_search[i][j]
        rows[i].append(char)
        cols[j].append(char)
        fdiags[i + j].append(char)
        bdiags[i - j].append(char)

rows = map("".join, rows)
cols = map("".join, cols)
fdiags = map("".join, fdiags)
bdiags = map("".join, bdiags)

for row in rows:
    count += count_xmas(row)

for col in cols:
    count += count_xmas(col)

for fdiag in fdiags:
    count += count_xmas(fdiag)

for bdiag in bdiags:
    count += count_xmas(bdiag)

print(count)
