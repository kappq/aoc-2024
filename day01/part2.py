left_list = []
right_list = []

with open("input.txt") as f:
    for line in f.readlines():
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

similarity = 0

for n in left_list:
    similarity += n * right_list.count(n)

print(similarity)
