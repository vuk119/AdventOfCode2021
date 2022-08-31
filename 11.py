def print_m(octs):
    return
    for o in octs:
        print(o)

    print("\n")

def valid_position(i, j):
    not_valid = i < 0 or i >= len(octs) or j < 0 or j >= len(octs[0])
    return not not_valid

def dfs(i, j, flashed, octs):
    if not valid_position(i, j):
        return # Invalid position

    if (i, j) in flashed:
        return
    if octs[i][j] <= 9:
        return


    flashed.add((i, j))
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di != 0 or dj != 0:
                if not valid_position(i + di, j + dj):
                    continue
                octs[i + di][j + dj] += 1
                dfs(i + di, j + dj, flashed, octs)


def one_step(octs):
    flashed = set()

    # first increment each by 1
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            octs[i][j] += 1

    # count flashes and trigger more flashes
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            dfs(i, j, flashed, octs)

    sync = True
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            if octs[i][j] > 9:
                octs[i][j] = 0
            else:
                sync = False


    return len(flashed), sync


def solve1(octs, n_steps, second=False):
    n_flashes = 0
    n_steps = 100000000 if second else n_steps
    for k in range(n_steps):
        print_m(octs)
        step_flashes, sync = one_step(octs)
        if sync and second:
            print_m(octs)
            return k + 1
        n_flashes += step_flashes

    return n_flashes

with open("11.txt", "r") as file:
    s = file.read()

matrix = s[:-1].split('\n')
octs = [[int(energy_level) for energy_level in row] for row in matrix]
print_m(octs)
print(solve1(octs, 100, True))
