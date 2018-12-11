
def cell_power_level(x, y, serial):
    rack_id = x + 10
    power_level_start = rack_id * y
    power_level = power_level_start + serial
    power_level = power_level * rack_id
    hundreds_digit = int(str(power_level)[-3]) if power_level >= 100 else 0
    return hundreds_digit - 5


def compute_grid(size, serial):
    grid = []
    for x in range(0, size-1):
        line = []
        for y in range(0, size-1):
            line.append(cell_power_level(x, y, serial))
        grid.append(line)
    return grid


def find_highest_square(grid):
    max_val = None
    max_pos = (None, None)
    for x in range(len(grid)-2):
        for y in range(len(grid[x])-2):
            total = grid[x][y] + grid[x][y+1] + grid[x][y+2] + \
                grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2] + \
                grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2]
            if not max_val or total > max_val:
                max_val = total
                max_pos = (x, y)
    return max_pos


tests = {
    (3, 5, 8): 4,
    (122, 79, 57): -5,
    (217, 196, 39): 0,
    (101, 153, 71): 4,
}

for test_input, expected in tests.items():
    print(test_input, "yielded", cell_power_level(*test_input), "expected", expected)

print("Highest square with serial 18 is", find_highest_square(compute_grid(300, 18)), "expected 33, 45")
print("Highest square with serial 42 is", find_highest_square(compute_grid(300, 42)), "expected 21, 61")
print("Highest square with serial 1308 is", find_highest_square(compute_grid(300, 1308)))
