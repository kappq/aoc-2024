left_list = []
right_list = []

with open("input.txt") as f:
    for line in f.readlines():
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

sum = 0

while left_list and right_list:
    min_left = min(left_list)
    min_right = min(right_list)

    sum += abs(min_left - min_right)

    left_list.remove(min_left)
    right_list.remove(min_right)

print(sum)
