from statistics import median, mean


def solve1(positions) -> int:

    m = median(positions)

    cost = lambda positions, m: sum([abs(m - p) for p in positions])

    return int(min(cost(positions, m), cost(positions, m + 1)))

def solve2(positions) -> int:

    med = median(positions)
    avg = mean(positions)

    l = min(med, avg)
    r = max(med, avg)
    l = int(l) - 1
    r = int(r) + 1

    cost = lambda positions, y: sum([abs(x-y) * (abs(x-y) + 1) / 2 for x in positions])

    return min([cost(positions, p) for p in range(l, r+1)])

with open("7.txt", "r") as f:
    s = f.read()

positions = [int(n) for n in s.split(',')]

print(solve1(positions))
print(mean(positions), median(positions))
print(solve2([16,1,2,0,4,2,7,1,2,14]))
print(solve2(positions))
