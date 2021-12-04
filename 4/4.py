def play_bingo():
    for num in rng:
        for i in range(len(boards)):
            if not bingoed[i]:
                for j in range(len(boards[i])):
                    for k in range(len(boards[i][j])):
                        if num == boards[i][j][k]:
                            flags[i][j][k] = True
                            # now check row and col of flagged.
                            # hardcoded 5
                            if (
                                flags[i][0][k]
                                and flags[i][1][k]
                                and flags[i][2][k]
                                and flags[i][3][k]
                                and flags[i][4][k]
                            ) or (
                                flags[i][j][0]
                                and flags[i][j][1]
                                and flags[i][j][2]
                                and flags[i][j][3]
                                and flags[i][j][4]
                            ):
                                print("bingo baby!")
                                print("Board number" + str(i))
                                bingoed[i] = True
                                # time to calculate score.
                                score = 0
                                for l in range(len(flags[i])):
                                    for m in range(len(flags[i][l])):
                                        if not flags[i][l][m]:
                                            score += int(boards[i][l][m])
                                print(score * int(num))
                                # return


if __name__ == "__main__":
    with open("input.txt") as f:
        rng = next(f).rstrip(("\n")).split(",")
        # print(rng)
        # skip new line after rng
        next(f)
        boards = []
        inner = []
        for i in f.readlines():
            if i == "\n":
                boards.append(inner)
                inner = []
            else:
                inner.append(i.rstrip("\n").split())
        boards.append(inner)
        # print(outer)
        # if any("999" in sublist for sublist in boards[0]):
        #     print("exists")
        flags = [
            [[False for x in range(5)] for y in range(5)] for i in range(len(boards))
        ]
        bingoed = [False for i in range(len(boards))]
        # print(flags)
        play_bingo()

# class board
# attributes:
# hard code 5x5 bingoboard
# 2d arr ( boarD)
# 2d arr (flags)
# on insert, check row and check col to see if all flagged. if 1 not flagged, continue.
#
