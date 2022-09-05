import numpy as np
import matplotlib.pyplot as plt

def perform_single_fold(points, single_fold):
    axis = single_fold[0]
    fold = single_fold[1]

    points_set = set()
    for point in points:
        x, y = point
        if axis == 'x':
            if x < fold:
                points_set.add((x, y))
            else:
                points_set.add((fold - (x - fold), y))
        elif axis == 'y':
            if y < fold:
                points_set.add((x, y))
            else:
                points_set.add((x, fold - (y - fold)))
        else:
            print("ERROR")


    return list(points_set)

def solve2(points, folds):

    for fold in folds:
        points = perform_single_fold(points, fold)

    x_max = -1
    y_max = -1

    for point in points:
        x_max = max(x_max, point[0])
        y_max = max(y_max, point[1])


    matrix = [[0] * (y_max + 1) for _ in range(x_max + 1)]

    for point in points:
        matrix[point[0]][point[1]] = 1

    print(x_max, y_max)
    for row in matrix:
        print(row)

    plt.imshow(np.array(matrix).T)
    plt.show()

def solve1(points, single_fold):
    return len(perform_single_fold(points, single_fold))

with open("13.txt", "r") as f:

    points = []
    folds = []
    x_max = -1
    y_max = -1
    for line in f.readlines():
        split1 = line.split(",")
        if len(split1) > 1:
            x, y = (int(split1[0]), int(split1[1][:-1]))
            x_max = max(x_max, x)
            y_max = max(y_max, y)
            points.append((x, y))
        else:
            if line != '\n':
                split2 = split1[0].split("=")
                if len(split2) > 1:
                    folds.append((split2[0][-1], int(split2[1])))

print(solve1(points, folds[0]))

print(solve2(points, folds))
