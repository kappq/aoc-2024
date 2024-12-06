from copy import deepcopy


with open("input.txt") as f:
    lab_map = [list(line) for line in f.readlines()]

width, height = len(lab_map[0]), len(lab_map)

guard_dir = None
guard_pos = None
for y, row in enumerate(lab_map):
    for x, col in enumerate(row):
        if col in ('^', 'v', '>', '<'):
            guard_dir = col
            guard_pos = (x, y)

if guard_dir is None or guard_pos is None:
    print("Guard not found")
    quit(1)

OFFSETS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
ROTATIONS = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


def detect_loop(lab_map, guard_dir, guard_pos):
    visited = set()

    while True:
        if (guard_dir, guard_pos) in visited:
            return True

        visited.add((guard_dir, guard_pos))

        offset = OFFSETS[guard_dir]

        new_pos = (guard_pos[0] + offset[0], guard_pos[1] + offset[1])
        new_x, new_y = new_pos

        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            return False

        if lab_map[new_y][new_x] == "#":
            guard_dir = ROTATIONS[guard_dir]
        else:
            guard_pos = new_pos


result = 0

for y in range(height):
    for x in range(width):
        lab_map_copy = deepcopy(lab_map)
        lab_map_copy[y][x] = "#"
        if detect_loop(lab_map_copy, guard_dir, guard_pos):
            result += 1

print(result)
