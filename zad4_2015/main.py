numbers = []

with open("liczby.txt") as file:
    numbers = file.read().splitlines()

more_zeros = 0

for number in numbers:
    zeros = number.count('0')
    ones = number.count('1')

    if zeros > ones:
        more_zeros += 1

divisable_by_two = 0
divisable_by_eight = 0

for number in numbers:
    if number[-1:] != "0":
        divisable_by_two += 1

for number in numbers:
    if number[-3:] == "000":
        divisable_by_eight += 1

decimals = []
for number in numbers:
    decimals.append(int(number, 2))

minimum = float("inf")
min_row = 0
maksimum = float("-inf")
max_row = 0

for index, number in enumerate(decimals):
    if number < minimum:
        minimum = number
        min_row = index + 1
    if number > maksimum:
        maksimum = number
        max_row = index + 1

with open("wyniki.txt", "w") as file:
    file.write("4.1: {}\n".format(more_zeros))
    file.write("4.2: {}, {}\n".format(divisable_by_two, divisable_by_eight))
    file.write("4.3: {}, {}\n".format(min_row, max_row))