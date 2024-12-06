with open("input.txt") as f:
    word_search = list(map(str.strip, f.readlines()))

width, height = len(word_search[0]), len(word_search)

count = 0

for i in range(height - 2):
    for j in range(width - 2):
        word1 = word_search[i][j] + word_search[i + 1][j + 1] + word_search[i + 2][j + 2]
        word2 = word_search[i][j + 2] + word_search[i + 1][j + 1] + word_search[i + 2][j]
        if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
            count += 1

print(count)
