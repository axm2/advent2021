def count_one_four_seven_eight(input):
    counter = 0
    signal_patterns = [[signal.split() for signal in line.split("|")] for line in input]
    for signal_pattern in signal_patterns:
        for digit in signal_pattern[1]:
            if len(digit) in [2, 4, 3, 7]:
                counter += 1
    return counter


def unscramble_signal(input):
    counter = 0
    signal_patterns = [[signal.split() for signal in line.split("|")] for line in input]
    total = 0
    for signal_pattern in signal_patterns:
        output_value = ""
        h = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
        five_digits = []
        six_digits = []
        f = ""
        c = ""
        e = ""
        b = ""
        # identify one,four,seven,eight and count digits for five and six digit num
        for digit in signal_pattern[0]:
            if len(digit) == 2:
                h[1] = digit
            elif len(digit) == 3:
                h[7] = digit
            elif len(digit) == 4:
                h[4] = digit
            elif len(digit) == 5:
                five_digits.append(digit)
            elif len(digit) == 6:
                six_digits.append(digit)
            elif len(digit) == 7:
                h[8] = digit
        # identify six
        for digit in six_digits:
            if not set(h[1]).issubset(set(digit)):
                h[6] = digit
        # isolate f and c
        for char in h[1]:
            if char in h[6]:
                f = char
            else:
                c = char
        # identify two, three and five
        for digit in five_digits:
            if c in digit and f in digit:
                h[3] = digit
            elif c in digit and f not in digit:
                h[2] = digit
            elif c not in digit and f in digit:
                h[5] = digit
        # isolate b and e
        for char in h[2]:
            if char not in h[3]:
                e = char
        for char in h[5]:
            if char not in h[3]:
                b = char
        # identify zero and nine
        for digit in six_digits:
            if c in digit and f in digit and b in digit and e in digit:
                h[0] = digit
            elif c in digit and f in digit and b in digit and e not in digit:
                h[9] = digit
        # flatten hashmap (oh no)
        key_list = list(h.keys())
        # val_list = list(h.values())
        val_list = [set(value) for value in h.values()]
        for digit in signal_pattern[1]:
            for i in range(len(val_list)):
                if val_list[i] == set(digit):
                    # print(key_list[i])
                    output_value += str(key_list[i])
        # print(output_value)
        total += int(output_value)
    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [i.rstrip("\n") for i in f.readlines()]
    # print(count_one_four_seven_eight(lines))
    unscramble_signal(lines)
