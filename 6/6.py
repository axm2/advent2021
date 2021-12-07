def simulate_fish(arr):
    counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for fish in arr:
        counter[fish] = counter.get(fish, 0) + 1
    for i in range(256):
        for i in range(0, 10):
            if i == 0:
                # rolled into 7 and 9 because we will subtract later, making it roll into 6 and 8 respectively.
                counter[7] = counter.get(7, 0) + counter[0]
                counter[9] = counter[0]
            else:
                counter[i - 1] = counter[i]
                counter[i] = 0
    print(counter)
    print(sum(counter.values()))


if __name__ == "__main__":
    with open("input.txt") as f:
        lanternfish = [int(x) for x in next(f).rstrip("\n").split(",")]
    simulate_fish(lanternfish)
