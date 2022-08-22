def solve1(commads) -> int:
    depth = 0
    position = 0

    for c in commands:
        if c[0] == "forward":
            position += c[1]
        if c[0] == "down":
            depth += c[1]
        if c[0] == "up":
            depth -= c[1]

    return depth * position

def solve2(commads) -> int:
    depth = 0
    position = 0
    aim = 0

    for c in commands:
        if c[0] == "forward":
            position += c[1]
            depth += aim * c[1]
        if c[0] == "down":
            aim += c[1]
        if c[0] == "up":
            aim -= c[1]

    return depth * position

with open("2.txt", "r") as file:
    s = file.read()

commands = [d.split(" ") for d in s.split('\n')]
commands = [(c[0], int(c[1])) for c in commands[:-1]]

print(solve1(commands))
print(solve2(commands))
