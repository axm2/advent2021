def simulate_octopuses(input):
    # input = [[energy + 1 for energy in line] for line in input]
    # make a deque
    # place all over 9 in the deque
    # grab from front, flash it(increment surrounding)
    # if any that increase go over 9, then place it at the back of the queue.
    # continue until queue finished
    # keep a list of coords that have flashed to avoid flashing twice, and also to have a running count of who flashed.

    # need to avoid edges every time we check or flash.
    flash_counter = 0
    for step in range(1000):
        flash_queue = []
        for i in range(len(input)):
            for j in range(len(input[i])):
                input[i][j] += 1
                if input[i][j] > 9:
                    flash_queue.append((i, j))
        flashed = set(flash_queue)

        # flash
        while not len(flash_queue) == 0:
            # flash 9 surrounding cells
            # don't go over bounds
            # hard code, we know its a 10 by 10
            # if x = 0 or x = 9
            # if y = 0 or y = 9
            coord = flash_queue.pop(0)

            # middle
            if 0 < coord[0] < len(input) - 1 and 0 < coord[1] < len(input) - 1:
                # safe to flash all 8 coords
                input[coord[0] - 1][coord[1] - 1] += 1
                if input[coord[0] - 1][coord[1] - 1] > 9 and (coord[0] - 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] - 1))
                    flashed.add((coord[0] - 1, coord[1] - 1))

                input[coord[0] + 1][coord[1] - 1] += 1
                if input[coord[0] + 1][coord[1] - 1] > 9 and (coord[0] + 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] - 1))
                    flashed.add((coord[0] + 1, coord[1] - 1))

                input[coord[0] + 1][coord[1] + 1] += 1
                if input[coord[0] + 1][coord[1] + 1] > 9 and (coord[0] + 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] + 1))
                    flashed.add((coord[0] + 1, coord[1] + 1))

                input[coord[0] - 1][coord[1] + 1] += 1
                if input[coord[0] - 1][coord[1] + 1] > 9 and (coord[0] - 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] + 1))
                    flashed.add((coord[0] - 1, coord[1] + 1))

                input[coord[0]][coord[1] - 1] += 1
                if input[coord[0]][coord[1] - 1] > 9 and (coord[0], coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] - 1))
                    flashed.add((coord[0], coord[1] - 1))

                input[coord[0] - 1][coord[1]] += 1
                if input[coord[0] - 1][coord[1]] > 9 and (coord[0] - 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1]))
                    flashed.add((coord[0] - 1, coord[1]))

                input[coord[0]][coord[1] + 1] += 1
                if input[coord[0]][coord[1] + 1] > 9 and (coord[0], coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] + 1))
                    flashed.add((coord[0], coord[1] + 1))

                input[coord[0] + 1][coord[1]] += 1
                if input[coord[0] + 1][coord[1]] > 9 and (coord[0] + 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1]))
                    flashed.add((coord[0] + 1, coord[1]))
            ## corners
            # top left corner
            elif coord[0] == 0 and coord[1] == 0:
                # flash 3
                input[coord[0] + 1][coord[1] + 1] += 1
                if input[coord[0] + 1][coord[1] + 1] > 9 and (coord[0] + 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] + 1))
                    flashed.add((coord[0] + 1, coord[1] + 1))

                input[coord[0]][coord[1] + 1] += 1
                if input[coord[0]][coord[1] + 1] > 9 and (coord[0], coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] + 1))
                    flashed.add((coord[0], coord[1] + 1))

                input[coord[0] + 1][coord[1]] += 1
                if input[coord[0] + 1][coord[1]] > 9 and (coord[0] + 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1]))
                    flashed.add((coord[0] + 1, coord[1]))

            # bottom right corner
            elif coord[0] == len(input) - 1 and coord[1] == len(input) - 1:
                input[coord[0] - 1][coord[1] - 1] += 1
                if input[coord[0] - 1][coord[1] - 1] > 9 and (coord[0] - 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] - 1))
                    flashed.add((coord[0] - 1, coord[1] - 1))

                input[coord[0]][coord[1] - 1] += 1
                if input[coord[0]][coord[1] - 1] > 9 and (coord[0], coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] - 1))
                    flashed.add((coord[0], coord[1] - 1))

                input[coord[0] - 1][coord[1]] += 1
                if input[coord[0] - 1][coord[1]] > 9 and (coord[0] - 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1]))
                    flashed.add((coord[0] - 1, coord[1]))

            elif coord[0] == 0 and coord[1] == len(input) - 1:
                input[coord[0] + 1][coord[1] - 1] += 1
                if input[coord[0] + 1][coord[1] - 1] > 9 and (coord[0] + 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] - 1))
                    flashed.add((coord[0] + 1, coord[1] - 1))

                input[coord[0] + 1][coord[1]] += 1
                if input[coord[0] + 1][coord[1]] > 9 and (coord[0] + 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1]))
                    flashed.add((coord[0] + 1, coord[1]))

                input[coord[0]][coord[1] - 1] += 1
                if input[coord[0]][coord[1] - 1] > 9 and (coord[0], coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] - 1))
                    flashed.add((coord[0], coord[1] - 1))

            elif coord[0] == len(input) - 1 and coord[1] == 0:
                input[coord[0] - 1][coord[1] + 1] += 1
                if input[coord[0] - 1][coord[1] + 1] > 9 and (coord[0] - 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] + 1))
                    flashed.add((coord[0] - 1, coord[1] + 1))

                input[coord[0] - 1][coord[1]] += 1
                if input[coord[0] - 1][coord[1]] > 9 and (coord[0] - 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1]))
                    flashed.add((coord[0] - 1, coord[1]))

                input[coord[0]][coord[1] + 1] += 1
                if input[coord[0]][coord[1] + 1] > 9 and (coord[0], coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] + 1))
                    flashed.add((coord[0], coord[1] + 1))

            ## plus
            elif coord[0] == 0 and 0 < coord[1] < len(input) - 1:
                # flash 5
                input[coord[0] + 1][coord[1] - 1] += 1
                if input[coord[0] + 1][coord[1] - 1] > 9 and (coord[0] + 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] - 1))
                    flashed.add((coord[0] + 1, coord[1] - 1))

                input[coord[0] + 1][coord[1] + 1] += 1
                if input[coord[0] + 1][coord[1] + 1] > 9 and (coord[0] + 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] + 1))
                    flashed.add((coord[0] + 1, coord[1] + 1))

                input[coord[0]][coord[1] - 1] += 1
                if input[coord[0]][coord[1] - 1] > 9 and (coord[0], coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] - 1))
                    flashed.add((coord[0], coord[1] - 1))

                input[coord[0]][coord[1] + 1] += 1
                if input[coord[0]][coord[1] + 1] > 9 and (coord[0], coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] + 1))
                    flashed.add((coord[0], coord[1] + 1))

                input[coord[0] + 1][coord[1]] += 1
                if input[coord[0] + 1][coord[1]] > 9 and (coord[0] + 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1]))
                    flashed.add((coord[0] + 1, coord[1]))

            elif coord[0] == len(input) - 1 and 0 < coord[1] < len(input) - 1:
                input[coord[0] - 1][coord[1] + 1] += 1
                if input[coord[0] - 1][coord[1] + 1] > 9 and (coord[0] - 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] + 1))
                    flashed.add((coord[0] - 1, coord[1] + 1))

                input[coord[0]][coord[1] - 1] += 1
                if input[coord[0]][coord[1] - 1] > 9 and (coord[0], coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] - 1))
                    flashed.add((coord[0], coord[1] - 1))

                input[coord[0] - 1][coord[1]] += 1
                if input[coord[0] - 1][coord[1]] > 9 and (coord[0] - 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1]))
                    flashed.add((coord[0] - 1, coord[1]))

                input[coord[0]][coord[1] + 1] += 1
                if input[coord[0]][coord[1] + 1] > 9 and (coord[0], coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] + 1))
                    flashed.add((coord[0], coord[1] + 1))

                input[coord[0] - 1][coord[1] - 1] += 1
                if input[coord[0] - 1][coord[1] - 1] > 9 and (coord[0] - 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] - 1))
                    flashed.add((coord[0] - 1, coord[1] - 1))

            elif 0 < coord[0] < len(input) - 1 and coord[1] == 0:
                input[coord[0] - 1][coord[1]] += 1
                if input[coord[0] - 1][coord[1]] > 9 and (coord[0] - 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1]))
                    flashed.add((coord[0] - 1, coord[1]))

                input[coord[0]][coord[1] + 1] += 1
                if input[coord[0]][coord[1] + 1] > 9 and (coord[0], coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] + 1))
                    flashed.add((coord[0], coord[1] + 1))

                input[coord[0] + 1][coord[1]] += 1
                if input[coord[0] + 1][coord[1]] > 9 and (coord[0] + 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1]))
                    flashed.add((coord[0] + 1, coord[1]))

                input[coord[0] + 1][coord[1] + 1] += 1
                if input[coord[0] + 1][coord[1] + 1] > 9 and (coord[0] + 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] + 1))
                    flashed.add((coord[0] + 1, coord[1] + 1))

                input[coord[0] - 1][coord[1] + 1] += 1
                if input[coord[0] - 1][coord[1] + 1] > 9 and (coord[0] - 1, coord[1] + 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] + 1))
                    flashed.add((coord[0] - 1, coord[1] + 1))

            elif 0 < coord[0] < len(input) - 1 and coord[1] == len(input) - 1:
                input[coord[0] + 1][coord[1]] += 1
                if input[coord[0] + 1][coord[1]] > 9 and (coord[0] + 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1]))
                    flashed.add((coord[0] + 1, coord[1]))

                input[coord[0]][coord[1] - 1] += 1
                if input[coord[0]][coord[1] - 1] > 9 and (coord[0], coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0], coord[1] - 1))
                    flashed.add((coord[0], coord[1] - 1))

                input[coord[0] - 1][coord[1]] += 1
                if input[coord[0] - 1][coord[1]] > 9 and (coord[0] - 1, coord[1]) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1]))
                    flashed.add((coord[0] - 1, coord[1]))

                input[coord[0] - 1][coord[1] - 1] += 1
                if input[coord[0] - 1][coord[1] - 1] > 9 and (coord[0] - 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] - 1, coord[1] - 1))
                    flashed.add((coord[0] - 1, coord[1] - 1))

                input[coord[0] + 1][coord[1] - 1] += 1
                if input[coord[0] + 1][coord[1] - 1] > 9 and (coord[0] + 1, coord[1] - 1) not in flashed:
                    flash_queue.append((coord[0] + 1, coord[1] - 1))
                    flashed.add((coord[0] + 1, coord[1] - 1))

        # reset
        for i in range(len(input)):
            for j in range(len(input[i])):
                if input[i][j] > 9:
                    input[i][j] = 0
        flash_counter += len(flashed)
        if len(flashed) == 100:
            print("ALLFLASHED!")
            print(step + 1)
            return

    print(input)
    print(flash_counter)


if __name__ == "__main__":
    with open("11/input.txt") as f:
        lines = [[int(char) for char in i.rstrip("\n")] for i in f.readlines()]
    simulate_octopuses(lines)
