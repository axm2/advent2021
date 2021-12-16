import heapq


def shortest_path(map):
    # pick a route, calc the cost so far
    # if the route becomes too expensive, choose another route?
    # how to keep track of what we visited and what we need to visit?
    finished = False
    prio_q = []
    # we start at 0,0 so lets push that on the q
    heapq.heappush(prio_q, (0, (0, 0)))
    checks = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    seen = set()
    while not finished:
        # pop the cheapest route so far, push all the surrounding choices. then continue until we get to the end?
        coord = heapq.heappop(prio_q)
        if coord[1][0] == len(map) - 1 and coord[1][1] == len(map[0]) - 1:
            finished = True
            print(coord[0])
            return
        if coord[1] not in seen:
            seen.add(coord[1])
            for c in checks:
                i, j = coord[1][0] + c[0], coord[1][1] + c[1]
                if (0 <= i < len(map)) and (0 <= j < len(map[0])):
                    heapq.heappush(prio_q, (map[i][j] + coord[0], (i, j)))


if __name__ == "__main__":
    with open("15/input.txt") as f:
        lines = [[int(char) for char in i.rstrip("\n")] for i in f.readlines()]
    lines5 = [
        [((num + i + j - 1) % 9) + 1 for i in range(0, 5) for num in line] for j in range(0, 5) for line in lines
    ]
    shortest_path(lines5)
