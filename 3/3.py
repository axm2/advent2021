def read_diagnostic_report():
    gamma = ""
    for i in range(len(lines[0])):
        zeros = 0
        for line in lines:
            if line[i] == "0":
                zeros += 1
        if zeros > len(lines) // 2:
            # more zeros than ones
            gamma += "0"
        else:
            gamma += "1"
    print(gamma)
    epsilon = "".join("1" if x == "0" else "0" for x in gamma)
    print(epsilon)
    print(int(epsilon, 2) * int(gamma, 2))


def get_generator_rating(report, idx):
    ones = 0
    zeros = 0
    zeros_report = []
    ones_report = []
    if len(report) == 1:
        # print(report[0])
        return report[0]
    else:
        for line in report:
            if line[idx] == "0":
                zeros += 1
                zeros_report.append(line)
            else:
                ones += 1
                ones_report.append(line)
        if ones >= zeros:
            return get_generator_rating(ones_report, idx + 1)
        else:
            return get_generator_rating(zeros_report, idx + 1)


def get_scrubber_rating(report, idx):
    ones = 0
    zeros = 0
    zeros_report = []
    ones_report = []
    if len(report) == 1:
        # print(report[0])
        return report[0]
    else:
        for line in report:
            if line[idx] == "0":
                zeros += 1
                zeros_report.append(line)
            else:
                ones += 1
                ones_report.append(line)
        if zeros <= ones:
            return get_scrubber_rating(zeros_report, idx + 1)
        else:
            return get_scrubber_rating(ones_report, idx + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [i.rstrip("\n") for i in f.readlines()]
    # read_diagnostic_report()
    gr = get_generator_rating(lines, 0)
    sr = get_scrubber_rating(lines, 0)
    print(int(gr, 2) * int(sr, 2))
