def find_all_rules(page):
    next_rules = []
    for rule in rules:
        if page == rule[0]:
            next_rules.append(rule[1])
    return next_rules


with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules.split()]
    updates = [tuple(map(int, update.split(","))) for update in updates.split()]

sum = 0

for update in updates:
    is_wrong = False
    for i, page_a in enumerate(update):
        next_rules = find_all_rules(page_a)
        for rule in next_rules:
            for page_b in update[:i]:
                if rule == page_b:
                    is_wrong = True
                    break
        if is_wrong:
            break
    if not is_wrong:
        sum += update[int(len(update) / 2)]

print(sum)
