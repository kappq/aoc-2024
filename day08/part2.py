with open("input.txt") as f:
    freqs = [line.strip() for line in f.readlines()]

width, height = len(freqs[0]), len(freqs)

antinodes = set()

for y1 in range(height):
    for x1 in range(width):
        freq1 = freqs[y1][x1]
        if freq1 == ".":
            continue

        for y2 in range(height):
            for x2 in range(width):
                freq2 = freqs[y2][x2]
                if freq2 == ".":
                    continue

                if freq1 == freq2 and (x1, y1) != (x2, y2):
                    antinodes.add((x1, y1))
                    antinodes.add((x2, y2))

                    x_diff = x1 - x2
                    y_diff = y1 - y2

                    ant1 = (x1 + x_diff, y1 + y_diff)
                    while 0 <= ant1[0] < width and 0 <= ant1[1] < height:
                        antinodes.add(ant1)
                        ant1 = (ant1[0] + x_diff, ant1[1] + y_diff)

                    ant2 = (x2 - x_diff, y2 - y_diff)
                    while 0 <= ant2[0] < width and 0 <= ant2[1] < height:
                        antinodes.add(ant2)
                        ant2 = (ant2[0] - x_diff, ant2[1] - y_diff)

print(len(antinodes))
