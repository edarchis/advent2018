from itertools import combinations


# returns the common section between strings only if one char difference, otherwise None
def common_section(str1, str2):
    # position of the single difference
    diff_pos = -1
    # would normally account for different string lengths if outside AoC
    for i, char in enumerate(str1):
        if char != str2[i]:
            if diff_pos > -1:  # second difference, GTFO
                return None
            diff_pos = i
    if diff_pos > -1:
        return str1[:diff_pos] + str1[diff_pos+1:]
    else:
        return None


def find_contiguous_boxes(box_list):
    # We should probably optimize this lookup to avoid testing every combination but this works
    for i, j in combinations(box_list, 2):
        common = common_section(i, j)
        if common:
            return common


test_input = [
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "fguij",
    "axcye",
    "wvxyz",
]

print("test: ", find_contiguous_boxes(test_input))
print("real: ", find_contiguous_boxes(open("input.txt")))
