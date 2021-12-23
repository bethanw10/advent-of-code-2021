from parse import *


def print_grid(path, target_x1, target_x2, target_y1, target_y2):
    all_points = path + [(target_x1, target_y1), (target_x2, target_y2)]

    min_x = min(all_points, key=lambda k: k[0])[0]
    min_y = min(all_points, key=lambda k: k[1])[1]

    max_x = max(all_points, key=lambda k: k[0])[0]
    max_y = max(all_points, key=lambda k: k[1])[1]

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) == (0, 0):
                print('S', end='')
            elif (x, y) in path:
                print('#', end='')
            elif target_x1 <= x <= target_x2 and target_y1 <= y <= target_y2:
                print('T', end='')
            else:
                print('.', end='')
        print()


def test_velocity(dx, dy, target_x1, target_x2, target_y1, target_y2):
    x, y = 0, 0
    path = [(x, y)]
    while True:
        x += dx
        y += dy
        path.append((x, y))

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        dy -= 1

        if target_x1 <= x <= target_x2 and target_y1 <= y <= target_y2:
            return True, path

        if y < target_y1:
            return False, path


def part_one(target_x1, target_x2, target_y1, target_y2):
    coords = (0, 0)
    highest_y = 0

    for x in range(target_x2):
        for y in range(target_y1, 1000, 1):
            reaches_target, path = test_velocity(x, y, target_x1, target_x2, target_y1, target_y2)

            if reaches_target:
                _, max_y = max(path, key=lambda k: k[1])

                if max_y > highest_y:
                    coords = (x, y),
                    highest_y = max_y

    print(coords, highest_y)


def part_two(target_x1, target_x2, target_y1, target_y2):
    num_velocities = 0

    for x in range(0, target_x2 + 100):
        for y in range(target_y1, 1000):
            reaches_target, path = test_velocity(x, y, target_x1, target_x2, target_y1, target_y2)

            if reaches_target:
                num_velocities += 1

    print(num_velocities)


def main():
    file = open("input.txt", "r").read()
    x1, x2, y1, y2 = parse("target area: x={}..{}, y={}..{}", file)

    part_one(int(x1), int(x2), int(y1), int(y2))
    part_two(int(x1), int(x2), int(y1), int(y2))


if __name__ == "__main__":
    main()
