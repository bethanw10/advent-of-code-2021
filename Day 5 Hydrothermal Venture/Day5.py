def part_one(lines):
    vent_map = {}

    for line in lines:
        p1, p2 = line.split(" -> ")

        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")

        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            for y in range(int(min_y), int(max_y) + 1):
                if (x1, y) in vent_map:
                    vent_map[(x1, y)] += 1
                else:
                    vent_map[(x1, y)] = 1
        elif y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)

            for x in range(int(min_x), int(max_x) + 1):
                if (x, y1) in vent_map:
                    vent_map[(x, y1)] += 1
                else:
                    vent_map[(x, y1)] = 1

    overlaps = sum(num_vents > 1 for num_vents in vent_map.values())

    print("Overlaps:", overlaps)


def part_two(lines):
    vent_map = {}

    for line in lines:
        p1, p2 = line.split(" -> ")

        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")

        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        dx = 0
        if x1 != x2:
            dx = 1 if x2 > x1 else -1

        dy = 0
        if y1 != y2:
            dy = 1 if y2 > y1 else -1

        x, y = x1, y1

        while x != x2 + dx or y != y2 + dy:
            if (x, y) in vent_map:
                vent_map[(x, y)] += 1
            else:
                vent_map[(x, y)] = 1

            x += dx
            y += dy

    overlaps = sum(num_vents > 1 for num_vents in vent_map.values())

    print("Overlaps:", overlaps)


def main():
    file = open("input.txt", "r")
    lines = file.read().split('\n')

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
