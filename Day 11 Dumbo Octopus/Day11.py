import copy


def part_one(grid):
    # print_octopuses(grid)
    num_flashes = 0

    for step in range(100):
        num_flashes += simulate(grid)

        # print(step)
        # print_octopuses(grid)

    print("Number of flashes:", num_flashes)


def part_two(grid):
    # print_octopuses(grid)
    num_steps = 0
    num_flashes = 0
    while num_flashes != 100:
        num_steps += 1
        num_flashes = simulate(grid)

        # print(num_steps)
        # print_octopuses(grid)

    print("Number of steps:", num_steps)


def simulate(grid):
    num_flashes = 0

    # First increase all by 1
    for x, line in enumerate(grid):
        for y, number in enumerate(line):
            grid[x][y] += 1

    any_flashes = True
    already_flashed = []

    # Then simulate flashes
    while any_flashes:
        any_flashes = False

        for x, line in enumerate(grid):
            for y, number in enumerate(line):
                if number > 9 and (x, y) not in already_flashed:
                    already_flashed.append((x, y))
                    any_flashes = True
                    num_flashes += 1

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            adj_x = x + dx
                            adj_y = y + dy

                            if (dx, dy) != (0, 0) and in_range(adj_x, adj_y, grid):
                                grid[adj_x][adj_y] += 1

    # Then any octopus that flashed reset to 0
    for x, line in enumerate(grid):
        for y, number in enumerate(line):
            if number > 9:
                grid[x][y] = 0

    return num_flashes


def in_range(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])


def print_octopuses(octopuses):
    for line in octopuses:
        for number in line:
            if number == 0:
                print(f'\033[93m{str(number)}\033[0m ', end='')
            else:
                print(str(number) + " ", end='')
        print()
    print()


def main():
    file = open("input.txt", "r")
    inputs = [[int(c) for c in line] for line in file.read().split('\n')]

    part_one(copy.deepcopy(inputs))
    part_two(copy.deepcopy(inputs))


if __name__ == "__main__":
    main()
