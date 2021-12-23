def part_one(commands):
    depth = 0
    horizontal_pos = 0

    for command in commands:
        direction, value = command.split(' ')
        value = int(value)

        if direction == "forward":
            horizontal_pos += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value

        print(depth, horizontal_pos)

    print("Final position:", depth * horizontal_pos)


def part_two(commands):
    depth = 0
    horizontal_pos = 0
    aim = 0

    for command in commands:
        direction, value = command.split(' ')
        value = int(value)

        if direction == "forward":
            horizontal_pos += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value

        print(depth, horizontal_pos)

    print("Final position:", depth * horizontal_pos)


def main():
    file = open("input.txt", "r")
    lines = file.read().split('\n')

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()

