def folder(transparent_paper, instructions):
    total_dots = 0
    for direction, fold_coord in instructions:
        if direction == "x":
            max_y = 0
            new_coords = set()
            coords_to_discard = set()
            for x, y in transparent_paper:
                if max_y < y:
                    max_y = y
                if x > int(fold_coord):
                    new_coords.add(((int(fold_coord) * 2) - x, y))
                    coords_to_discard.add((x, y))
            transparent_paper = (transparent_paper - coords_to_discard) | new_coords
            print(len(transparent_paper))
        if direction == "y":
            max_x = 0
            new_coords = set()
            coords_to_discard = set()
            for x, y in transparent_paper:
                if max_x < x:
                    max_x = x
                if y > int(fold_coord):
                    new_coords.add((x, (int(fold_coord) * 2) - y))
                    coords_to_discard.add((x, y))
            transparent_paper = (transparent_paper - coords_to_discard) | new_coords
            print(len(transparent_paper))

    print_paper(transparent_paper)


def print_paper(transparent_paper):
    max_X = 0
    max_Y = 0
    for x, y in transparent_paper:
        if x > max_X:
            max_X = x
        if y > max_Y:
            max_Y = y
    for i in range(max_Y + 1):
        for j in range(max_X + 1):
            if (j, i) not in transparent_paper:
                print(".", end="")
            else:
                print("#", end="")
        print()


if __name__ == "__main__":
    with open("13/input.txt") as f:
        lines = {
            tuple(int(coord) for coord in line.rstrip("\n").split(","))
            for line in f.readlines()
            if line[0].isnumeric()
        }
        f.seek(0)
        instructions = [line[11:].rstrip("\n").split("=") for line in f.readlines() if line[0] == "f"]
    # print(lines)
    # print(instructions)
    folder(lines, instructions)
