#######################################################################################
# OK, this seemed like an easy day. It got painful to understand exactly how it was
# supposed to work. This is a big trial and error. It's ugly and everything but
# it works.
# If I had to improve it, I would extend the row of pots and return the updated offset.
# I originally didn't read the part with the checksum. Otherwise, I would have started
# differently. I know, I should read better. What can I say ? I did this while writing
# some actually useful code for which I'm paid and helping my kids get ready for exams.
#
# Now, seeing how part 2 is making this whole thing worthless, I'll have to rethink
# the approach completely.
# I will probably leave this part as is and write a whole new app for part 2 now.
#######################################################################################

import copy
import re

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


def new_gen(initial, rules):
    new_row = copy.copy(initial)
    for i in range(2, len(initial) - 2):
        new_row[i] = "."
        for rule, rule_result in rules:
            if initial[i - 2:i + 3] == rule:
                new_row[i] = rule_result
                break
    return new_row


def compute_value(pots, offset):
    foo = [i-offset if x == "#" else 0 for i, x in enumerate(pots)]
    return sum(foo)


sample_initial, sample_rules = load_file("sample.txt")
# This is dirty because the grid should be expandable but I didn't feel like wasting time rewriting this, so this works
sample_initial = ["." for _ in range(20)] + sample_initial + ["." for _ in range(20)]
print("gen1 gave:", "".join(new_gen(sample_initial, sample_rules)))
print("expected :", "                  ..#...#....#.....#..#..#..#...")

next_gen = sample_initial
for i in range(1, 21):
    next_gen = new_gen(next_gen, sample_rules)
    print(i, "".join(next_gen))

print("computed value", compute_value(next_gen, 20), "expected 325")

actual_initial, actual_rules = load_file("input.txt")
actual_initial = ["." for _ in range(20)] + actual_initial + ["." for _ in range(20)]
next_gen = actual_initial
for i in range(1, 21):
    next_gen = new_gen(next_gen, actual_rules)
    print(i, "".join(next_gen))

print("computed value", compute_value(next_gen, 20))
