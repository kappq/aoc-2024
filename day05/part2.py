def find_all_next_rules(page):
    next_rules = []
    for rule in rules:
        if page == rule[0]:
            next_rules.append(rule[1])
    return next_rules


with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.split()]
    updates = [list(map(int, update.split(","))) for update in updates.split()]

sum = 0

incorrect_updates = []

for update in updates:
    is_wrong = False
    for i, page_a in enumerate(update):
        next_rules = find_all_next_rules(page_a)
        for rule in next_rules:
            for page_b in update[:i]:
                if rule == page_b:
                    is_wrong = True
                    break
        if is_wrong:
            break
    if is_wrong:
        incorrect_updates.append(update)

for update in incorrect_updates:
    for i in range(len(update)):
        for j in range(i, len(update)):
            page_a, page_b = update[i], update[j]
            for rule in rules:
                if page_a == rule[1] and page_b == rule[0]:
                    update[i], update[j] = page_b, page_a
    sum += update[int(len(update) / 2)]

print(sum)
