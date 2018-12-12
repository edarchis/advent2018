import copy
import re
import time

re_initial = re.compile(r"initial state: ([.#]*)")
re_rule = re.compile(r"([.#]*) => ([.#])")


def load_file(filename):
    file = open(filename)
    initial = list(re_initial.match(file.readline()).group(1))
    rules = []
    for line in file.readlines():
        match = re_rule.match(line)
        if match:
            rules.append((list(match.group(1)), match.group(2)))
    return initial, rules


def new_gen(initial, rules, offset):
    initial = [".", ".", ".", "."] + initial + [".", ".", ".", "."]
    new_row = copy.copy(initial)
    for i in range(2, len(initial) - 2):
        new_row[i] = "."
        for rule, rule_result in rules:
            if initial[i - 2:i + 3] == rule:
                new_row[i] = rule_result
                break
    compacted_row, compacted_offset = compact_row(new_row, offset - 4)
    return compacted_row, compacted_offset


# transforms ("....#..#.", -2) to (#..#, 2)
def compact_row(row, offset):
    first_plant_index = next((i for i, x in enumerate(row) if x == '#'), 0)
    last_plant_index = len(row) - next((i for i, x in enumerate(reversed(row)) if x == '#'), 0)
    compacted = row[first_plant_index:last_plant_index]
    offset += first_plant_index
    return compacted, offset


def compute_value(pots, offset):
    foo = [i + offset if x == "#" else 0 for i, x in enumerate(pots)]
    return sum(foo)


def compute_generations(row, offset, rules, generations, verbose=True):
    row = copy.copy(row)
    prev_row = row  # find repeating patterns (shifting mostly)
    prev_offset = offset
    for i in range(generations):
        row, offset = new_gen(row, rules, offset)
        if row == prev_row:
            # we have a cycle, see how many generations there were still to add and compute the final value
            to_go = generations - i - 1
            offset_diff = offset - prev_offset
            final_offset = offset + to_go * offset_diff
            print("cycle found", prev_offset, offset, to_go, offset_diff, final_offset)
            return row, final_offset
        else:
            prev_row = row
            prev_offset = offset
        if verbose or i % int(generations / 100) == 0:
            print("gen", i + 1, "".join(row), offset, compute_value(row, offset))

    return row, offset


print("compact0:", compact_row(list("#.....#"), 0))
print("compact1:", compact_row(list(".....#.....#"), 0))
print("compact1:", compact_row(list("...#.....#..."), 3))

sample_initial, sample_rules = load_file("sample.txt")
gen1, gen1_offset = new_gen(sample_initial, sample_rules, 0)
print("gen1 gave:", gen1_offset, "".join(gen1))
print("expected :", 0, "#...#....#.....#..#..#..#")

t0 = time.time()
sample20, sample20_offset = compute_generations(sample_initial, 0, sample_rules, 20)
print("computed value", compute_value(sample20, sample20_offset), "expected 325")
print("computed in", time.time() - t0)

t0 = time.time()
actual_initial, actual_rules = load_file("input.txt")
actual20, actual20_offset = compute_generations(actual_initial, 0, actual_rules, 20)
print("computed value", compute_value(actual20, actual20_offset))
print("computed in", time.time() - t0)

t0 = time.time()
actual_big, actual_big_offset = compute_generations(actual_initial, 0, actual_rules, 50000000000, verbose=True)
print("computed value", compute_value(actual_big, actual_big_offset))
print("computed in", time.time() - t0)
