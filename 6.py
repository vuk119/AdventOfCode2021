import sys

def compute_single(timer, days_left, dp, first):
    # how many fishes you have starting with one fish with timer and N

    if timer == -1:
        first = False
        timer = 6

    if (timer, days_left, first) in dp:
        return dp[(timer, days_left, first)]

    if days_left == 0:
        if timer == 6 and first is False:
            return 2
        return 1

    if timer == 6 and first is False:
        sol = compute_single(timer - 1, days_left - 1, dp, first) + compute_single(7, days_left - 1, dp, True)
        dp[(timer, days_left, first)] = sol
        return sol

    sol = compute_single(timer - 1, days_left - 1, dp, first)
    dp[(timer, days_left, first)] = sol
    return sol


def solve1(timers, days_left) -> int:

    dp = dict()

    return sum([compute_single(t, days_left, dp, False) for t in timers])


with open("6.txt", "r") as f:
    s = f.read()

timers = [int(n) for n in s.split(',')]
print(solve1(timers, 80))
print(solve1(timers, 256))
