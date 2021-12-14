from collections import Counter
import copy


def polymer_simulator(template, rules):
    char_counter = Counter(template)
    polymer_pairs = {}
    for (ele_A, ele_B) in zip(template[:-1], template[1:]):
        s = ele_A + ele_B
        if s in polymer_pairs:
            polymer_pairs[ele_A + ele_B] += 1
        else:
            polymer_pairs[ele_A + ele_B] = 1
    for i in range(40):
        temp = copy.deepcopy(polymer_pairs)
        # we need to calc all additions indep from checking polypair. maybe copy the hmap?
        # like check on the before, and then work on the after.
        for polymer_pair in temp.keys():
            j = temp[polymer_pair]
            new_ele = rules[polymer_pair]
            if new_ele not in char_counter:
                char_counter[new_ele] = j
            else:
                char_counter[new_ele] += j
            if polymer_pair[0] + new_ele not in polymer_pairs:
                polymer_pairs[polymer_pair[0] + new_ele] = j
            else:
                polymer_pairs[polymer_pair[0] + new_ele] += j
            if new_ele + polymer_pair[1] not in polymer_pairs:
                polymer_pairs[new_ele + polymer_pair[1]] = j
            else:
                polymer_pairs[new_ele + polymer_pair[1]] += j
            polymer_pairs[polymer_pair] -= j
    # calc score
    least_common = char_counter.most_common()[-1]
    most_common = char_counter.most_common()[0]
    print(most_common[1] - least_common[1])
    print(polymer_pairs)
    print(char_counter)


if __name__ == "__main__":
    with open("14/input.txt") as f:
        template = next(f).rstrip(("\n"))
        next(f)
        rules_list = [line.strip().split(" -> ") for line in f.readlines()]
        rules = dict(rules_list)
    polymer_simulator(template, rules)
