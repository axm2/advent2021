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
    checks = set((i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)) - {0, 0}
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
            # flash 8 surrounding cells
            # don't go over bounds
            coord = flash_queue.pop(0)
            # https://github.com/alelouis/advent-of-code/blob/master/2021/day-11/main.py
            for c in checks:
                i, j = coord[0] + c[0], coord[1] + c[1]
                if (0 <= i < 10) and (0 <= j < 10):
                    input[i][j] += 1
                    if input[i][j] > 9 and (i, j) not in flashed:
                        flash_queue.append((i, j))
                        flashed.add((i, j))

        # reset
        for flashed_octo in flashed:
            input[flashed_octo[0]][flashed_octo[1]] = 0
        flash_counter += len(flashed)
        if len(flashed) == 100:
            print("ALLFLASHED!")
            print(step + 1)
            return

    print(input)
    print(flash_counter)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [[int(char) for char in i.rstrip("\n")] for i in f.readlines()]
    simulate_octopuses(lines)
