from itertools import cycle

input_file = open("input.txt", "r")
freq_list = [int(x) for x in input_file]
frequency = 0
found_frequencies = {}

for shift in cycle(freq_list):
    frequency += shift
    print(f"frequency: {frequency}, shifted {shift}")
    if found_frequencies.get(frequency):
        print(f"Already found frequency {frequency}")
        break
    else:
        found_frequencies[frequency] = True
