from copy import copy


def react(original_polymer):
    polymer = copy(original_polymer)
    i = 0
    while i < len(polymer) - 1:
        if polymer[i] == polymer[i + 1].swapcase():
            polymer = polymer[:i] + polymer[i + 2:]
            i -= 1 if i > 0 else 0  # check the previous character again as it might now react
        else:
            i += 1
    return polymer


print("aA:", react("aA"), len(react("aA")))
print("abBA:", react("abBA"), len(react("abBA")))
print("abAB:", react("abAB"), len(react("abAB")))
print("aabAAB:", react("aabAAB"), len(react("aabAAB")))
print("dabAcCaCBAcCcaDA:", react("dabAcCaCBAcCcaDA"), len(react("dabAcCaCBAcCcaDA")))

actual_polymer = react(open("input.txt").readline())
print("solution:", len(actual_polymer))
