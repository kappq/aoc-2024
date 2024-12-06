reports = []

with open("input.txt") as f:
    for line in f.readlines():
        levels = list(map(int, line.split()))
        reports.append(levels)

def check_safety(report):
    sequence_type = None
    if report[0] < report[1]:
        sequence_type = "inc"
    elif report[0] > report[1]:
        sequence_type = "dec"

    for level1, level2 in zip(report, report[1:]):
        diff = level1 - level2
        if abs(diff) < 1 or abs(diff) > 3 or (sequence_type == "inc" and diff > 0) or (sequence_type == "dec" and diff < 0):
            return False

    return True


n_safe = 0

for report in reports:
    if check_safety(report):
        n_safe += 1

print(n_safe)
