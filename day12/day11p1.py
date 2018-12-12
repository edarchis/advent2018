import re

re_initial = re.compile(r"initial state: ([.#]*)")
re_rule = re.compile(r"([.#]*) => ([.#])")


def load_file(filename):
    file = open(filename)
    initial = re_initial.match(file.readline()).group(1)
    rules = {}
    for line in file.readlines():
        match = re_rule.match(line)
        if match:
            rules[match.group(1)]=match.group(2)
    return initial, rules


def new_gen(initial, rules):
    row = ".." + initial + ".."
    new_row = ""
    for i in range(len(initial)):
        print(f"processing {i}: {row[i+2]}")
        result = "."
        for rule, rule_result in rules.items():
            if row[i:i+5] == rule:
                result = rule_result
                break
        new_row += result
    return new_row


sample_initial, sample_rules = load_file("sample.txt")
new = new_gen(sample_initial, sample_rules)
print("foo")
