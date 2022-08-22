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

with open("3.txt", "r") as file:
    s = file.read()

numbers = s.split("\n")[:-1]
print(solve1(numbers))
