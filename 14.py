class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def add(self, val):
        old_next = self.next
        new_node = Node(val, old_next)
        self.next = new_node

    def init_head(polymer):
        
        cur_head = Node(polymer[-1])

        for i in range(len(polymer)-2, -1, -1):
            cur_head = Node(polymer[i], cur_head)

        return cur_head

    def to_string(self):

        s = f"{self.value}"
        
        node = self
        while not node.next is None:
            node = node.next
            s += f"{node.value}"
        
        return s

def insert(str, pos, char):
    return str[:pos] + char + str[pos:] 

def n_steps(polymer, rules, n):

    for i in range(n):
        polymer = one_step(polymer, rules)

    return polymer

def one_step_node(polymer, rules):
    
    inserts = [] # (position, character)

    for r in rules:
        first = r[0]
        second = r[1]
        middle = r[-1]
        head = polymer
        i = 0
        while not head.next is None:
            if head.value == first and head.next.value == second:
                inserts.append((i + 1, middle))
            head = head.next
            i = i + 1
    inserts.sort(key = lambda x: x[0])
    
    head = polymer
    cnt = 1

    for insrt in inserts:

        while cnt < insrt[0]:
            cnt += 1
            head = head.next
    
        head.add(insrt[1])
        head = head.next

    return polymer

def one_step_node_quick(polymer: Node, rules_dict):
    
    head = polymer
    while not head.next is None:
        # Consider all rules between head and the next
        if (head.value, head.next.value) in rules_dict:
            head.add(rules_dict[(head.value, head.next.value)])
            head = head.next.next # Skip the one you just added
        else:
            head = head.next # No insert just proceed

    return polymer

def n_steps_node(polymer, rules, n):
    for i in range(n):
        print(i)
        polymer = one_step_node(polymer, rules)

    return polymer

def one_step(polymer, rules):
    
    inserts = [] # (position, character)

    for r in rules:
        first = r[0]
        second = r[1]
        middle = r[-1]

        for i in range(len(polymer) - 1):
            if polymer[i] == first and polymer[i + 1] == second:
                inserts.append((i + 1, middle))

    
    inserts.sort(key = lambda x: x[0])
    shift = 0

    for insrt in inserts:
        polymer = insert(polymer, insrt[0] + shift, insrt[1])
        shift += 1

    return polymer

def solve1(polymer, rules):

    polymer = n_steps(polymer, rules, 10)

    counts = {}

    min_c = 1000000000000000000000000000
    max_c = -1

    for c in polymer:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1


    for c in counts.values():
        min_c = min(c, min_c)
        max_c = max(c, max_c)

    print(min_c, max_c)
    print(counts)
    return max_c - min_c

def solve2(polymer, rules):

    polymer = n_steps_node(polymer, rules, 40)

    counts = {}

    min_c = 1000000000000000000000000000
    max_c = -1

    while not polymer is None:
        if polymer.value not in counts:
            counts[polymer.value] = 1
        else:
            counts[polymer.value] += 1
        polymer = polymer.next

    for c in counts.values():
        min_c = min(c, min_c)
        max_c = max(c, max_c)

    print(min_c, max_c)
    print(counts)
    return max_c - min_c

def solve_quick(polymer, rules, n):

    rules_dict = {}
    for rule in rules:
        a = rule[0]
        b = rule[1]

        c = rule[-1]

        rules_dict[(a, b)] = c
    
    for kk in range(n):
        print("Doing", kk)
        polymer = one_step_node_quick(polymer, rules_dict)

    counts = {}

    min_c = 1000000000000000000000000000
    max_c = -1

    while not polymer is None:
        if polymer.value not in counts:
            counts[polymer.value] = 1
        else:
            counts[polymer.value] += 1
        polymer = polymer.next

    for c in counts.values():
        min_c = min(c, min_c)
        max_c = max(c, max_c)

    print(min_c, max_c)
    print(counts)
    return max_c - min_c

def get_all_and_rules_pairs(rules):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = [l for l in letters]
    cnt = [0 for l in letters]

    letters_cnt = dict(zip(letters, cnt))

    all_pairs = {}
    for l in letters:
        for r in letters:
            all_pairs[(l, r)] = 0

    rules_pairs = {}
    for r in rules:
        rules_pairs[(r[0], r[1])] = r[-1]

    return letters_cnt, all_pairs, rules_pairs

def solve_quickest(polymer, rules, n):
    first = polymer[0]
    last = polymer[-1]

    letters_cnt, all_pairs, rules_pairs = get_all_and_rules_pairs(rules)

    for l in polymer:
        letters_cnt[l] += 1

    init_pairs = [(polymer[i], polymer[i+1]) for i in range(len(polymer) - 1)]
    static_pairs = [pair for pair in init_pairs if pair not in rules_pairs]
    non_static_pairs = [pair for pair in init_pairs if pair in rules_pairs]

    for i in range(n):
        print("Doing", i, len(non_static_pairs))
        new_non_static_pairs = []

        for pair in non_static_pairs:
            l, r = pair
            m = rules_pairs[(l, r)]
            letters_cnt[m] += 1

            if (l, m) in rules_pairs:
                new_non_static_pairs.append((l, m))
            else:
                static_pairs.append((l, m))
            if (m, r) in rules_pairs:
                new_non_static_pairs.append((m, r))
            else:
                static_pairs.append((m, r))
        
        non_static_pairs = new_non_static_pairs
    


    return letters_cnt

def solve_quickest_final(polymer, rules, n):
    first = polymer[0]
    last = polymer[-1]

    letters_cnt, all_pairs, rules_pairs = get_all_and_rules_pairs(rules)
    for l in polymer:
            letters_cnt[l] += 1

    init_pairs = [(polymer[i], polymer[i+1]) for i in range(len(polymer) - 1)]
    static_pairs = [pair for pair in init_pairs if pair not in rules_pairs]
    non_static_pairs = [pair for pair in init_pairs if pair in rules_pairs]

    non_static_pairs_dict = {}

    for pair in non_static_pairs:
        if pair not in non_static_pairs_dict:
            non_static_pairs_dict[pair] = 1
        else:
            non_static_pairs_dict[pair] += 1
    
    

    for i in range(n):
        new_non_static_pairs_dict = {}
        for pair in non_static_pairs_dict.keys():
            l, r = pair
            cnt = non_static_pairs_dict[pair]
            m = rules_pairs[(l, r)]
            letters_cnt[m] += cnt

            if (l, m) in rules_pairs:
                if (l, m) in new_non_static_pairs_dict:
                    new_non_static_pairs_dict[(l, m)] += cnt
                else:
                    new_non_static_pairs_dict[(l, m)] = cnt
            
            if (m, r) in rules_pairs:
                if (m, r) in new_non_static_pairs_dict:
                    new_non_static_pairs_dict[(m, r)] += cnt
                else:
                    new_non_static_pairs_dict[(m, r)] = cnt
        
        non_static_pairs_dict = new_non_static_pairs_dict
    
    max_cnt = -1
    min_cnt = 100000000000000000000000000000000000
    for l in letters_cnt.keys():
        if letters_cnt[l] != 0:
            max_cnt = max(max_cnt, letters_cnt[l])
            min_cnt = min(min_cnt, letters_cnt[l])


    return max_cnt - min_cnt

with open("14.txt", "r") as file:
    s = file.read().split("\n")

polymer = s[0]
rules = s[2:]

polymer_node = Node.init_head(polymer)

# print(solve1(polymer, rules))
# print(solve_quick(polymer_node, rules, 10))

print(solve_quickest_final(polymer, rules, 10))
print(solve_quickest_final(polymer, rules, 40))