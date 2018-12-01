input_file = open("input.txt", "r")

frequency = 0
for shift in input_file:
    frequency += shift

print(frequency)
