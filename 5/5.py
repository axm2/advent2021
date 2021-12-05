import re


def find_overlaps():
    total_overlaps = 0
    h = {}
    for first_pair, second_pair in coordinate_pairs:
        # consider only horizontal and vertical lines
        if first_pair[0] == second_pair[0]:
            points = list(
                range(
                    min(int(first_pair[1]), int(second_pair[1])),
                    1 + max(int(first_pair[1]), int(second_pair[1])),
                )
            )
            for point in points:
                # print(first_pair[0] + "," + str(point))
                if first_pair[0] + "," + str(point) in h:
                    h[first_pair[0] + "," + str(point)] += 1
                else:
                    h[first_pair[0] + "," + str(point)] = 1

        elif first_pair[1] == second_pair[1]:
            points = list(
                range(
                    min(int(first_pair[0]), int(second_pair[0])),
                    1 + max(int(first_pair[0]), int(second_pair[0])),
                )
            )
            for point in points:
                # print(str(point) + "," + first_pair[1])
                if str(point) + "," + first_pair[1] in h:
                    h[str(point) + "," + first_pair[1]] += 1
                else:
                    h[str(point) + "," + first_pair[1]] = 1
        else:
            x_points = []
            y_points = []
            if int(first_pair[0]) < int(second_pair[0]):
                x_points = list(range(int(first_pair[0]), 1 + int(second_pair[0])))
            else:
                x_points = list(range(int(first_pair[0]), int(second_pair[0]) - 1, -1))
            if int(first_pair[1]) < int(second_pair[1]):
                y_points = list(range(int(first_pair[1]), 1 + int(second_pair[1])))
            else:
                y_points = list(range(int(first_pair[1]), int(second_pair[1]) - 1, -1))
            points = list(zip(x_points, y_points))
            for point in points:
                if str(point[0]) + "," + str(point[1]) in h:
                    h[str(point[0]) + "," + str(point[1])] += 1
                else:
                    h[str(point[0]) + "," + str(point[1])] = 1
    larger_elements = [element for element in list(h.values()) if element >= 2]
    print(len(larger_elements))


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [re.sub("[^0-9,-]", "", i).split("-") for i in f.readlines()]
        coordinate_pairs = [
            [coordinate.split(",") for coordinate in line] for line in lines
        ]
        find_overlaps()
