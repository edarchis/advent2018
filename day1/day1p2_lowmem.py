from itertools import cycle

# This version reads straight from the file to avoid loading it all into memory
input_file = open("input.txt", "r")
frequency = 0
found_frequencies = {}
found = False

while not found:
    for shift in input_file:
        frequency += int(shift)
        print(f"frequency: {frequency}, shifted {shift}")
        if found_frequencies.get(frequency):
            print(f"Already found frequency {frequency}")
            found = True
            break
        else:
            found_frequencies[frequency] = True
    input_file.seek(0)
    print("Looping back to the start of the input file")

input_file.close()
