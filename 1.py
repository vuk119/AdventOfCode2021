def solve1(depths : list[int]) -> int:
    i = 0
    cnt = 0
    while i < len(depths) - 1:
        if depths[i+1] > depths[i]:
            cnt += 1
        i += 1

    return cnt

def solve2(depths : list[int]) -> int:
    if len(depths) < 3:
        return 0

    first = 0
    last = 2
    cnt = 0

    while last != len(depths) - 1:

        if depths[last+1] - depths[first] > 0:
            cnt += 1

        last += 1
        first += 1

    return cnt

with open("1.txt", "r") as file:
    s = file.read()

depths = [int(d) for d in s.split('\n')]
print(solve1(depths))
print(solve2(depths))
