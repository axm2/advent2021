import copy
def parse_input(rough_map):
    h = {}
    for a, b in rough_map:
        h[a] = {b} if a not in h else h[a] | {b}
        h[b] = {a} if b not in h else h[b] | {a}
    return h

def count_paths(hmap, start_point, path, flag):
    if start_point == 'end':
        return 1
    if start_point.islower() and start_point in path:
        if flag == False:
            flag = True
        else:
            return 0
    path.append(start_point)
    total_points = 0
    for point_b in hmap[start_point]:
        if point_b != 'start':
            total_points+=count_paths(hmap, point_b, copy.copy(path), flag)
    return total_points


if __name__ == "__main__":
    with open("12/input.txt") as f:
        lines = [line.rstrip("\n").split("-") for line in f.readlines()]
    print(count_paths(parse_input(lines), "start", [], False))