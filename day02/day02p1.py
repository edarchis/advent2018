from collections import Counter
from functools import reduce


def has_doubles_and_triples(code):
    letter_count = Counter(code)
    return int(2 in letter_count.values()), int(3 in letter_count.values())


def compute_code(codelist):
    tot = reduce(
        lambda x, y: (x[0] + y[0], x[1] + y[1]),
        [has_doubles_and_triples(code) for code in codelist]
    )
    return tot[0] * tot[1]


def other_compute_code(codelist):
    dubs = 0
    trips = 0
    for code in codelist:
        d, t = has_doubles_and_triples(code)
        dubs += d
        trips += t
    return dubs * trips


test_input = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab",
]

test_expected = [
    (0, 0),
    (1, 1),
    (1, 0),
    (0, 1),
    (1, 0),  # aa and dd but count once
    (1, 0),
    (0, 1),  # aaa and bbb count once
]

for i in range(0, len(test_input)):
    print("test", i, test_input[i], has_doubles_and_triples(test_input[i]), test_expected[i])

print("test code", compute_code(test_input), "3*4=12")

print("actual code", compute_code(open("input.txt")))
