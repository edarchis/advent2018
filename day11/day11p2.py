def cell_power_level(x, y, serial):
    rack_id = x + 10
    power_level_start = rack_id * y
    power_level = power_level_start + serial
    power_level = power_level * rack_id
    hundreds_digit = int(str(power_level)[-3]) if power_level >= 100 else 0
    return hundreds_digit - 5


def compute_grid(size, serial):
    grid = []
    for x in range(0, size - 1):
        line = []
        for y in range(0, size - 1):
            line.append(cell_power_level(x, y, serial))
        grid.append(line)
    return grid


def find_highest_square(grid, grid_size):
    max_val = None
    max_pos = (None, None)
    for x in range(len(grid) - grid_size):
        for y in range(len(grid[x]) - grid_size):
            total = sum([sum(grid[i][y:y + grid_size]) for i in range(x, x + grid_size)])
            if not max_val or total > max_val:
                max_val = total
                max_pos = (x, y)
    return max_pos, max_val


def find_highest_square_size(grid, max_size_to_check):
    max_val = None
    max_pos = (None, None)
    max_size = None
    for size in range(2, max_size_to_check):
        print("checking size", size)
        pos, val = find_highest_square(grid, size)
        if not max_val or val > max_val:
            max_val = val
            max_pos = pos
            max_size = size
            print("found max", max_val, max_pos, max_size)
    return max_pos, max_size


tests = {
    (3, 5, 8): 4,
    (122, 79, 57): -5,
    (217, 196, 39): 0,
    (101, 153, 71): 4,
}

for test_input, expected in tests.items():
    print(test_input, "yielded", cell_power_level(*test_input), "expected", expected)

print("Highest square with serial 18 is", find_highest_square(compute_grid(300, 18), 3), "expected 33, 45")
print("Highest square with serial 42 is", find_highest_square(compute_grid(300, 42), 3), "expected 21, 61")
print("Highest square with serial 42 is", find_highest_square(compute_grid(300, 42), 3), "expected 21, 61")

print("Highest square with serial 1308 is", find_highest_square(compute_grid(300, 1308), 3))

print("Max anysize square with serial 18", find_highest_square_size(compute_grid(300, 18), 20), "expected 90,269,16")
print("Max anysize square with serial 42", find_highest_square_size(compute_grid(300, 42), 20), "expected 232,251,12")
print("Max anysize square with serial 1308", find_highest_square_size(compute_grid(300, 1308), 40))
