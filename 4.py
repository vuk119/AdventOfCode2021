def check_board(board_mask):
    # check rows
    for i in range(5):
        if sum(board_mask[i]) == 5:
            return True

    board_mask = list(map(list, zip(*board_mask)))
    for i in range(5):
        if sum(board_mask[i]) == 5:
            return True

def solution1(mask, dct) -> int:
    inv_dct = dict(zip(dct.values(), dct.keys()))

    sol = 0

    for i in range(5):
        for j in range(5):
            if not mask[i][j]:
                sol += inv_dct[(i, j)]


    return sol

def solve1(numbers, masks, dicts) -> int:

    for n in numbers:
        for i in range(len(dicts)):
            if n in dicts[i]:
                masks[i][dicts[i][n][0]][dicts[i][n][1]] = True
                if check_board(masks[i]):
                    print(i)
                    return n * solution1(masks[i], dicts[i])

def solve2(numbers, masks, dicts) -> int:

    boards_that_won = [False] * 100
    won_cnt = 0
    last_won = -1
    last_won_n = -1

    for n in numbers:
        for i in range(len(dicts)):
            if boards_that_won[i]:
                continue
            if n in dicts[i]:
                masks[i][dicts[i][n][0]][dicts[i][n][1]] = True
                if check_board(masks[i]):
                    last_won = i
                    last_won_n = n
                    boards_that_won[i] = True
                    if won_cnt == 99:
                        return n * solution1(masks[i], dicts[i])
                    won_cnt += 1

    return last_won_n * solution1(masks[last_won], dicts[last_won])


with open("4.txt", "r") as file:
    s = file.read()

s = s.split("\n")

i = 0
numbers = [int(n) for n in s[0].split(',')]
i = 2

boards = []
masks = []
dicts = []

locations = []
for j in range(5):
    row = []
    for k in range(5):
        row.append((j, k))
    locations.append(row)

while i < len(s):

    # Read 5 rows = 1 board
    board = []
    mask = []
    dct = {}
    for row in range(5):
        board.append([int(n) for n in s[i].split(' ') if n != ''])
        mask.append([False] * 5)
        dct.update(dict(zip(board[row], locations[row])))
        i += 1

    boards.append(board)
    masks.append(mask)
    dicts.append(dct)
    i += 1 # skip blank row

print(solve1(numbers, masks, dicts))
print(solve2(numbers, masks, dicts))
