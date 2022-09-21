import random
from queue import PriorityQueue

def get_neighbours(i, j, m, n):

    is_valid = lambda x, y: x < m and x > -1 and y < n and y > -1

    neighbours = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if (di == 0 or dj == 0) and di + dj != 0:
                if is_valid(i + di, j + dj):
                    neighbours.append((i + di, j + dj))

    return neighbours



def print_path(m, n, move):
    i, j = 0, 0

    while i != m-1 or j != n-1:
        print(i, j)
        i, j = move[(i, j)]


def generate_from_tile(di, dj, full_costs):
    m = len(full_costs) // 5
    n = len(full_costs[0]) // 5

    # Generate downwards
    if dj == 0:
        for i in range(m):
            for j in range(n):
                new_cost = full_costs[(di - 1) * m + i][j] + 1
                if new_cost == 10:
                    new_cost = 1
                full_costs[di * m + i][j] = new_cost
    else:
        for i in range(m):
            for j in range(n):
                new_cost = full_costs[di * m + i][(dj - 1) * n + j] + 1
                if new_cost == 10:
                    new_cost = 1
                full_costs[di * m + i][dj * n + j] = new_cost

def solve2(costs):
    n = len(costs[0])
    m = len(costs)
    full_costs = [[0 for _ in range(5 * m)] for __ in range(5 * n)]

    for i in range(m):
        for j in range(n):
            full_costs[i][j] = costs[i][j]

    # Generate downwards
    for di in range(1, 5):
        generate_from_tile(di, 0, full_costs)

    # Generate to the right
    for di in range(0, 5):
        for dj in range(1, 5):
            generate_from_tile(di, dj, full_costs)

    solve1(full_costs)


def solve1(costs):
    n = len(costs[0])
    m = len(costs)
    min_distance = [[10000000 for _ in c] for c in costs]
    min_distance[0][0] = 0
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        cost_so_far, (i, j) = pq.get()

        for (inn, jnn) in get_neighbours(i, j, m, n):
            new_cost = cost_so_far + costs[inn][jnn]
            if min_distance[inn][jnn] > new_cost:
                min_distance[inn][jnn] = new_cost
                pq.put((new_cost, (inn, jnn)))
    
    print(min_distance[m-1][n-1])


with open("15.txt", "r") as f:
    s = f.read()


costs = [[int(c) for c in ss if c != '\n'] for ss in s.split('\n')]



solve1(costs)
solve2(costs)