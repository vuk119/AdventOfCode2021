CHAR_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
MATCH = {')': '(', ']': '[', '}': '{', '>': '<'}
CHAR_SCORES2 = {'(': 1, '[': 2, '{': 3, '<': 4}

def get_score(line) -> int:
    stack = ['x']
    for i, c in enumerate(line):
        if c in ['[', '(', '<', '{']:
            stack.append(c)
        else:
            if len(stack) < 1:
                return CHAR_SCORES[c]
            if MATCH[c] != stack[-1]:
                return CHAR_SCORES[c]
            stack.pop()
    return 0

def get_score2(line) -> int:
    stack = []
    for i, c in enumerate(line):
        if c in ['[', '(', '<', '{']:
            stack.append(c)
        else:
            stack.pop()

    score = 0
    for c in stack[::-1]:
        score = score * 5 + CHAR_SCORES2[c]
    return score

def solve1(s) -> int:
    sum = 0
    for l in s:
        sum += get_score(l)
    return sum

def solve2(s) -> int:
    incomplete = [l for l in s if get_score(l) == 0]
    scores = []
    for l in incomplete:
        s = get_score2(l)
        scores.append(get_score2(l))

    return sorted(scores)[int(len(scores) / 2)]



with open("10.txt") as file:
    s = file.read().split('\n')[:-1]

print(solve1(s))
print(solve2(s))
