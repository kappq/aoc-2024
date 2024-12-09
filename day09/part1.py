with open("input.txt") as f:
    disk_map = list(map(int, f.read().strip()))

disk = []
for i, size in enumerate(disk_map):
    for _ in range(size):
        if i % 2 == 0:  # file
            disk.append(int(i / 2))
        else:  # free space
            disk.append(".")

k = 0
for i in reversed(range(len(disk))):
    if k >= i:
        break

    if disk[i] == ".":
        continue

    for j in range(k, i):
        if disk[j] == ".":
            disk[j] = disk[i]
            disk[i] = "."
            k = j
            break

checksum = sum([i * fid for i, fid in enumerate(disk) if fid != "."])
print(checksum)
