# Read in the input file.
with open("input.txt", "r") as myfile:
    input_file = [int(i.rstrip("\n")) for i in myfile.readlines()]


# def part_1():
#     increased_count = 0
#     for i in range(1, len(input_file)):
#         if input_file[i] > input_file[i - 1]:
#             increased_count += 1
#     return increased_count


# def part_2():
#     increased_count = 0
#     for i in range(3, len(input_file)):
#         if (
#             input_file[i - 2] + input_file[i - 1] + input_file[i]
#             > input_file[i - 1] + input_file[i - 2] + input_file[i - 3]
#         ):
#             increased_count += 1
#     return increased_count

def sliding_window_increasing_counter(window_size, input):
    increased_count = 0
    for i in range(window_size, len(input)):
        if sum(input[i-window_size+1:i+1])>sum(input[i-window_size:i]):
            increased_count+=1
    return increased_count

def main():
    # print("Part 1: " + str(part_1()))
    # print("Part 2: " + str(part_2()))
    print("Part 1: " + str(sliding_window_increasing_counter(1, input_file)))
    print("Part 2: " + str(sliding_window_increasing_counter(3, input_file)))


if __name__ == "__main__":
    main()
