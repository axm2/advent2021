def pilot_submarine(aim_flag):
    x_pos = 0
    y_pos = 0
    aim = 0
    for line in lines:
        direction, distance = line.split()
        if aim_flag==1:
            match direction:
                case "forward":
                    x_pos+=int(distance)
                    y_pos+=(aim*int(distance))
                case "down":
                    aim+=int(distance)
                case "up":
                    aim-=int(distance)
        else:
            match direction:
                case "forward":
                    y_pos+=int(distance)
                case "down":
                    x_pos+=int(distance)
                case "up":
                    x_pos-=int(distance)
    print(x_pos*y_pos)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [i.rstrip("\n") for i in f.readlines()]

    pilot_submarine(0)
    pilot_submarine(1)
