def part_one(dots, folds):
    grid = {}

    for dot in dots:
        x, y = dot.split(',')
        x, y = int(x), int(y)
        grid[(x, y)] = True

    fold = folds[0]
    _, _, fold = fold.split(' ')
    axis, value = fold.split('=')
    value = int(value)

    if axis == 'y':
        for coord, _ in grid.copy().items():
            x, y = coord
            if y > value:
                del grid[(x, y)]
                new_y = value - (y - value)
                grid[x, new_y] = True

    if axis == 'x':
        for coord, _ in grid.copy().items():
            x, y = coord
            if x > value:
                del grid[(x, y)]
                new_x = value - (x - value)
                grid[new_x, y] = True

    print("Num dots:", len(grid))


def part_two(dots, folds):
    grid = {}

    for dot in dots:
        x, y = dot.split(',')
        x, y = int(x), int(y)
        grid[(x, y)] = True

    for fold in folds:
        _, _, fold = fold.split(' ')
        axis, value = fold.split('=')
        value = int(value)

        if axis == 'y':
            for coord, _ in grid.copy().items():
                x, y = coord
                if y > value:
                    del grid[(x, y)]
                    grid[x, 2 * value - y] = True

        if axis == 'x':
            for coord, _ in grid.copy().items():
                x, y = coord
                if x > value:
                    del grid[(x, y)]
                    grid[2 * value - x, y] = True

    print_grid(grid)


def print_grid(grid):
    max_x = max(grid, key=lambda k: k[0])
    max_y = max(grid, key=lambda k: k[1])

    for y in range(max_y[1] + 1):
        for x in range(max_x[0] + 1):
            if (x, y) in grid:
                print('🟦', end='')
            else:
                print('🟧', end='')
        print()


def main():
    file = open("input.txt", "r")
    dots, folds = file.read().split('\n\n')
    folds = folds.split('\n')
    dots = dots.split('\n')

    part_one(dots, folds)
    part_two(dots, folds)


if __name__ == "__main__":
    main()
