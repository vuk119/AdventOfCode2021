class Node:

    def __init__(self, type_id):
        self.children = []
        self.type_id = type_id

        if self.type_id == 4:
            self.value = 0

    def add_child(self, n):
        self.children.append(n)

    def collapse_node(self):
        if self.type_id == 4:
            return
        else:
            for child in self.children:
                child.collapse_node()

            if self.type_id == 0:
                self.value = sum([child.value for child in self.children])

            elif self.type_id == 1:
                self.value = 1
                for child in self.children:
                    self.value *= child.value

            elif self.type_id == 2:
                self.value = min([child.value for child in self.children])

            elif self.type_id == 3:
                self.value = max([child.value for child in self.children])

            elif self.type_id == 5:
                self.value = 1 if self.children[0].value > self.children[1].value else 0

            elif self.type_id == 6:
                self.value = 1 if self.children[0].value < self.children[1].value else 0

            elif self.type_id == 7:
                self.value = 1 if self.children[0].value == self.children[1].value else 0
            
            else:
                assert False, "Wrong type_id"

            self.type_id = 4


def get_binary_repr(s):
    
    x = '''0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111'''


    x = [(s[0], s[-4:]) for s in x.split('\n')]
    mapping = dict(x)

    s_new = ""
    for c in s:
        s_new += mapping[c]
    
    return s_new

def get_number_from_binary(b):
    base = 1
    n = 0
    for c in b[::-1]:
        n += int(c) * base
        base *= 2
    
    return n

def get_trailing_zeros(diff):
    rounded_len = 0
    while rounded_len < diff:
        rounded_len += 4
    return rounded_len - diff

def dprint(s):
    if DEBUG:
        print(s)

SOL1 = [0]
DEBUG = False
def parse_packet(ptr, s, parent):
    
    dprint(f"\n Starting subpacket at {ptr}")

    start_ptr = ptr
    version = get_number_from_binary(s[ptr:ptr+3])
    SOL1[0] += version
    type_id = get_number_from_binary(s[ptr+3:ptr+6])

    node = Node(type_id)
    parent.add_child(node)

    dprint(f"Version {version} and type id {type_id}")
    number = ""
    ptr = ptr + 6
    
    if type_id == 4:
        while True:
            next_n_bin = s[ptr+1:ptr+5]
            number += next_n_bin
            ptr = ptr + 5
            if s[ptr-5] == '0':
                break
        trailing_zeros = 0 # get_trailing_zeros(ptr - start_ptr)
        number = get_number_from_binary(number)
        ptr += trailing_zeros

        node.value = number

        dprint(f"Found a literal from {start_ptr} to {ptr} with the value {number}")
    else:
        mode = s[ptr]
        ptr = ptr + 1

        if mode == '0':
            l = get_number_from_binary(s[ptr:ptr+15])
            ptr = ptr + 15

            dprint(f"subpackets length {l}")

            start_ptr = ptr
            while ptr - start_ptr < l:
                ptr = parse_packet(ptr, s, node)
            # ptr = ptr + l
        elif mode == '1':
            n_subpackets = get_number_from_binary(s[ptr:ptr+11])
            ptr = ptr + 11

            dprint(f"number of subpackets {n_subpackets}")

            for _ in range(n_subpackets):
                ptr = parse_packet(ptr, s, node)
        else:
            assert False, "Mode error."
        # Parse subpackets

    return ptr


def solve(s):

    s = get_binary_repr(s)
    ptr = 0

    root = Node(-1)

    # parse
    while ptr != len(s):

        try:
            ptr = parse_packet(ptr, s, root)
        except:
            print(s[ptr:])
            break
        if len(s[ptr:]) <= 4:
            break
    
    root.children[0].collapse_node()
    print(root.children[0].value)

with open("16.txt", "r") as f:
    s = f.read()

# solve1('C0015000016115A2E0802F182340')
solve(s)
print(SOL1)