with open("input.txt") as f:
    disk_map = list(map(int, f.read().strip()))

disk = []
for i, size in enumerate(disk_map):
    for _ in range(size):
        if i % 2 == 0:  # file
            disk.append(int(i / 2))
        else:  # free space
            disk.append(".")

i = len(disk) - 1
while i >= 0:
    if disk[i] == ".":
        i -= 1
        continue

    file_size = 0
    while disk[i - file_size] == disk[i]:
        file_size += 1

    j = 0
    while j < i:
        if disk[j] != ".":
            j += 1
            continue

        free_size = 0
        while disk[j + free_size] == ".":
            free_size += 1

        if file_size <= free_size:
            for k in range(file_size):
                disk[j + k] = disk[i - k]
                disk[i - k] = "."
            break

        j += free_size

    i -= file_size

checksum = sum([i * fid for i, fid in enumerate(disk) if fid != "."])
print(checksum)
