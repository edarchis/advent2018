input_file = open("input.txt", "r")

# Good: fast and uses nearly no memory, less good: good old procedural programming (I'd still go for this one)
frequency = 0
for shift in input_file:
    frequency += int(shift)

print(frequency)

input_file.seek(0)

# The drawback of this method is that it creates an array in memory before summing it
frequency2 = sum([int(shift) for shift in input_file])

print(frequency2)
