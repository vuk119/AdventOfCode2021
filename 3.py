def solve1(numbers) -> int:
    encoded = [0] * 12

    for number in numbers:
        for i, d in enumerate(number):
            if d == '0':
                encoded[i] -= 1
            elif d == '1':
                encoded[i] += 1

    gamma = [1 if int(n) > 0 else 0 for n in encoded]
    epsilon = [0 if int(n) > 0 else 1 for n in encoded]

    gamma = [gamma[i] * 2 ** (11 - i) for i in range(12)]
    epsilon = [epsilon[i] * 2 ** (11 - i) for i in range(12)]

    return sum(gamma) * sum(epsilon)

def step(numbers, flag, i) -> int:
    sum = 0

    for number in numbers:
        if number[i] == '0':
            sum -= 1
        elif number[i] == '1':
            sum += 1

    if flag:
        if sum >= 0:
            target = '1'
        else:
            target = '0'
    else:
        if sum >= 0:
            target = '0'
        else:
            target = '1'

    return [n for n in numbers if n[i]==target]


def solve2(numbers) -> int:

    oxygen = numbers
    i = 0
    while len(oxygen) > 1:
        oxygen = step(oxygen, True, i)
        i += 1
    oxygen = oxygen[0]
    oxygen_rating = [int(oxygen[i]) * 2 ** (11 - i) for i in range(12)]

    co2 = numbers
    i = 0
    while len(co2) > 1:
        co2 = step(co2, False, i)
        i += 1
    co2 = co2[0]
    co2_rating = [int(co2[i]) * 2 ** (11 - i) for i in range(12)]

    return sum(oxygen_rating) * sum(co2_rating)

with open("3.txt", "r") as file:
    s = file.read()

numbers = s.split("\n")[:-1]
print(solve1(numbers))
print(solve2(numbers))
