import numpy as np

class Line():

    def __init__(self, x0, y0, x1, y1):
        if x0 < x1 or y0 < y1:
            self.x0 = x0
            self.x1 = x1
            self.y0 = y0
            self.y1 = y1
        else:
            self.x0 = x1
            self.x1 = x0
            self.y0 = y1
            self.y1 = y0

    def get_points(self, is_one=True):
        if self.x0 == self.x1:
            return [(self.x0, y) for y in range(self.y0, self.y1 + 1)]
        if self.y0 == self.y1:
            return [(x, self.y0) for x in range(self.x0, self.x1 + 1)]
        if is_one:
            return None

        x_dir = -(self.x0 - self.x1) / abs(self.x0 - self.x1)
        y_dir = -(self.y0 - self.y1) / abs(self.y0 - self.y1)

        max_dif = abs(self.x0 - self.x1)

        return [(self.x0 + x_dir * i, self.y0 + y_dir * i) for i in range(max_dif + 1)]

    def __repr__(self):
        return f"({x0}, {y0}), ({x1}, {y1})"

def solve(lines, dim, is_one=True):
    points = np.zeros((dim+1, dim+1))
    cnt = 0
    for l in lines:
        ps = l.get_points(is_one)
        if ps is not None:
            for p in ps:
                x, y = p
                x = int(x)
                y = int(y)
                points[y, x] += 1
                if points[y, x] == 2 :
                    cnt += 1

    return cnt


lines = []
dim = 0
with open("5.txt", "r") as f:

    for l in f.readlines():
        l = l.split(" -> ")
        x0, y0 = [int(p) for p in l[0].split(",")]
        x1, y1 = [int(p) for p in l[1].split(",")]

        dim = max([dim, x0, y0, x1, y1])
        lines.append(Line(x0, y0, x1, y1))

print(solve(lines, dim))
print(solve(lines, dim, False))
