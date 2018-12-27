import re
from collections import namedtuple

Claim = namedtuple("Claim", ["id", "x", "y", "sx", "sy"])


def load_file(filename):
    matcher = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    claims = []
    for line in open(filename):
        matched = matcher.match(line)
        if matched:
            claims.append(
                Claim(
                    int(matched.group(1)),
                    int(matched.group(2)),
                    int(matched.group(3)),
                    int(matched.group(4)),
                    int(matched.group(5))
                )
            )
    return claims


def assign_segment(area, claim):
    # print("assigning claim", claim)
    for x in range(claim.x, claim.x + claim.sx):
        for y in range(claim.y, claim.y + claim.sy):
            # print("assigning", x, y)
            cell = area.get((x, y), [])
            if len(cell) > 0:
                print("found non empty cell", x, y, cell)
            cell.append(claim.id)
            area[(x, y)] = cell


def show_overlaps(area):
    for key, value in area.items():
        if len(value) > 1:
            print("cell", key[0], key[1], "is assigned to", value)


sample_area = {}
sample_claims = load_file("sample.txt")
for claim in sample_claims:
    assign_segment(sample_area, claim)
    print(claim)

overlaps = {k: v for k, v in sample_area.items() if len(v) > 1}
print(len(overlaps))
show_overlaps(sample_area)

actual_area = {}
actual_claims = load_file("input.txt")
for claim in actual_claims:
    assign_segment(actual_area, claim)
    print(claim)

overlaps = {k: v for k, v in actual_area.items() if len(v) > 1}
print(len(overlaps))

