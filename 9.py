def is_low_point(i, j, heights):

    is_low = True
    if i > 0:
        is_low = is_low and (heights[i][j] < heights[i-1][j])
    if j > 0:
        is_low = is_low and (heights[i][j] < heights[i][j-1])
    if i < len(heights) - 1:
        is_low = is_low and (heights[i][j] < heights[i+1][j])
    if j < len(heights[0]) - 1:
        is_low = is_low and (heights[i][j] < heights[i][j+1])

    return is_low

def solve1(heights) -> int:
    risk = 0
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if is_low_point(i, j, heights):
                risk += heights[i][j] + 1
    return risk

def get_basin_size(i, j, heights, visited, prev_val=None):

    if i < 0:
        return 0
    if j < 0:
        return 0
    if i >= len(heights):
        return 0
    if j >= len(heights[0]):
        return 0

    if heights[i][j] == 9:
        return 0

    if prev_val is not None:
        if heights[i][j] < prev_val + 1:
            return 0

    if (i, j) in visited:
        return 0

    visited.add((i, j))

    return 1 + get_basin_size(i-1, j, heights, visited, heights[i][j]) \
            + get_basin_size(i+1, j, heights, visited, heights[i][j]) \
            + get_basin_size(i, j-1, heights, visited, heights[i][j]) \
            + get_basin_size(i, j+1, heights, visited, heights[i][j])



def solve2(heights) -> int:

    basin_sizes = []

    for i in range(len(heights)):
        for j in range(len(heights[0])):

            if is_low_point(i, j, heights):
                visited = set()
                basin_sizes.append(get_basin_size(i, j, heights, visited))

    basin_sizes.sort()
    print(basin_sizes)


    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]



with open("9.txt", "r") as file:
    s = file.read()

heights1 = s.split("\n")[:-1]

heights = [[int(x) for x in [*heights1[i]]] for i in range(len(heights1))]


print(solve1(heights))
print(solve2(heights))
