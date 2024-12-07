equations = []

with open("input.txt") as f:
    for line in f.readlines():
        result, operands = line.split(": ")
        equations.append((int(result), list(map(int, operands.split()))))


def test_ops(result, curr, operands):
    if not operands and result == curr:
        return True
    elif not operands:
        return False

    result_plus = test_ops(result, curr + operands[0], operands[1:])
    result_mult = test_ops(result, curr * operands[0], operands[1:])
    result_conc = test_ops(result, int(str(curr) + str(operands[0])), operands[1:])

    return result_plus or result_mult or result_conc


tot = 0

for equation in equations:
    result, operands = equation
    if test_ops(result, operands[0], operands[1:]):
        tot += result

print(tot)
