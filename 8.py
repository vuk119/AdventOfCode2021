def solve1(outputs) -> int:
    cnt = 0
    for output in outputs:
        for digit in output.split(" "):
            if len(digit) in [2, 4, 3, 7]:
                cnt += 1

    return cnt

def get_mapping(inpt):
    digits = sorted(inpt.split(" "), key=lambda x: len(x))

    mapping = {}

    # Determine 1, 4, 7 and 8
    one = set([d for d in digits[0]])
    four = set([d for d in digits[2]])
    seven = set([d for d in digits[1]])
    eight = set([d for d in digits[-1]])


    # Determine what 'a' maps onto
    for n in seven:
        if n not in one:
            mapping['a'] = n

    # Determine 6
    zero_six_nine1 = set([d for d in digits[-2]])
    zero_six_nine2 = set([d for d in digits[-3]])
    zero_six_nine3 = set([d for d in digits[-4]])

    is_six = False
    for n in one:
        if n not in zero_six_nine1:
            is_six = True
            six = zero_six_nine1
            zero_nine1 = zero_six_nine2
            zero_nine2 = zero_six_nine3

    if not is_six:
        for n in one:
            if n not in zero_six_nine2:
                is_six = True
                six = zero_six_nine2
                zero_nine1 = zero_six_nine1
                zero_nine2 = zero_six_nine3

    if not is_six:
        for n in one:
            if n not in zero_six_nine3:
                is_six = True
                six = zero_six_nine3
                zero_nine1 = zero_six_nine1
                zero_nine2 = zero_six_nine2

    # Knowing 6 we can find 8 diff 6 which tells us the mapping of c
    for n in eight:
        if n not in six:
            mapping["c"] = n

    # Knowing "c" we can find "f" by looking at the remaining number from 1
    for n in one:
        if n != mapping["c"]:
            mapping["f"] = n


    # Find b or d by looking at 4
    b_or_d = []
    for n in four:
        if n != mapping["c"] and n != mapping["f"]:
            b_or_d.append(n)

    # Now look at 0 and 9. 0 has nly b while 9 has both. So determine b, d, 0 and 9.
    for n in b_or_d:
        if n not in zero_nine1:
            mapping["d"] = n
            mapping["b"] = [x for x in b_or_d if x != n][0]
            zero = zero_nine1
            nine = zero_nine2
        if n not in zero_nine2:
            mapping["d"] = n
            mapping["b"] = [x for x in b_or_d if x != n][0]
            zero = zero_nine2
            nine = zero_nine1

    # Now look at 8 diff 9 to find e
    for n in eight:
        if n not in nine:
            mapping["e"] = n

    # Find where g goes as it is the last one
    all = ["a", "b", "c", "d", "e", "f", "g"]
    for n in all:
        if n not in mapping.values():
            mapping["g"] = n

    return mapping

def decode_number(output, mapping):
    zero = set("a,b,c,e,f,g".split(','))
    one = set("c,f".split(','))
    two = set("a,c,d,e,g".split(','))
    three = set("a,c,d,f,g".split(','))
    four = set("b,c,d,f".split(','))
    five = set("a,b,d,f,g".split(','))
    six = set("a,b,d,e,f,g".split(','))
    seven = set("a,c,f".split(','))
    eight = set("a,b,c,d,e,f,g".split(','))
    nine = set("a,b,c,d,f,g".split(','))

    int_mapping = dict(zip(mapping.values(), mapping.keys()))


    number = ""
    for n in output.split(" "):
        decoded_n = set([int_mapping[c] for c in n])
        if decoded_n == zero:
            number += "0"
        if decoded_n == one:
            number += "1"
        if decoded_n == two:
            number += "2"
        if decoded_n == three:
            number += "3"
        if decoded_n == four:
            number += "4"
        if decoded_n == five:
            number += "5"
        if decoded_n == six:
            number += "6"
        if decoded_n == seven:
            number += "7"
        if decoded_n == eight:
            number += "8"
        if decoded_n == nine:
            number += "9"

    return int(number)


def solve2(lines):
    sum = 0

    for l in lines:
        inpt, output = l.split(" | ")
        mapping = get_mapping(inpt)
        sum += decode_number(output, mapping)

    return sum


with open("8.txt") as f:
    lines = f.read().split("\n")[:-1]


outputs = [l.split(" | ")[1] for l in lines]
print(solve1(outputs))
print(get_mapping("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"))
test = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
print(decode_number("cdfeb fcadb cdfeb cdbaf", get_mapping(test)))
print(solve2(lines))
