def find_low_points(heightmap):
    total_risk_level = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if i == len(heightmap) - 1 and j == len(heightmap[i]) - 1:
                if heightmap[i][j] < min(
                    heightmap[i - 1][j],
                    heightmap[i][j - 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif i == 0 and j == 0:
                if heightmap[i][j] < min(
                    heightmap[i + 1][j],
                    heightmap[i][j + 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif i == 0 and j == len(heightmap[i]) - 1:
                if heightmap[i][j] < min(
                    heightmap[i + 1][j],
                    heightmap[i][j - 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif i == len(heightmap) - 1 and j == 0:
                if heightmap[i][j] < min(
                    heightmap[i - 1][j],
                    heightmap[i][j + 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif i == 0:
                if heightmap[i][j] < min(
                    heightmap[i + 1][j],
                    heightmap[i][j - 1],
                    heightmap[i][j + 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif j == 0:
                if heightmap[i][j] < min(
                    heightmap[i - 1][j],
                    heightmap[i + 1][j],
                    heightmap[i][j + 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif i == len(heightmap) - 1:
                if heightmap[i][j] < min(
                    heightmap[i - 1][j],
                    heightmap[i][j - 1],
                    heightmap[i][j + 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif j == len(heightmap[i]) - 1:
                if heightmap[i][j] < min(
                    heightmap[i - 1][j],
                    heightmap[i + 1][j],
                    heightmap[i][j - 1],
                ):
                    total_risk_level += heightmap[i][j] + 1
            elif heightmap[i][j] < min(
                heightmap[i - 1][j],
                heightmap[i + 1][j],
                heightmap[i][j - 1],
                heightmap[i][j + 1],
            ):
                total_risk_level += heightmap[i][j] + 1
    return total_risk_level


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [[int(char) for char in i.rstrip("\n")] for i in f.readlines()]
    print(find_low_points(lines))
