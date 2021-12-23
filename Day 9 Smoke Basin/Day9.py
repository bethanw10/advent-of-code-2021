
def part_one(inputs):
    risk_level = 0

    for i, line in enumerate(inputs):
        for j, number in enumerate(line):
            is_lowest = True

            point = inputs[i][j]

            if i != 0 and inputs[i - 1][j] <= point:
                is_lowest = False

            if j != 0 and inputs[i][j - 1] <= point:
                is_lowest = False

            if i < len(inputs) - 1 and inputs[i + 1][j] <= point:
                is_lowest = False

            if j < len(inputs[i]) - 1 and inputs[i][j + 1] <= point:
                is_lowest = False

            if is_lowest:
                risk_level += point + 1

    print("Risk level:", risk_level)


def part_two(inputs):
    basin_sizes = []

    for i, line in enumerate(inputs):
        for j, number in enumerate(line):
            if number not in [9, -1]:
                basin = [(i, j)]
                tiles_to_check = [(i, j)]
                inputs[i][j] = -1

                while len(tiles_to_check) > 0:
                    new_tiles = []

                    for tile in tiles_to_check:
                        inputs[i][j] = -1
                        adjacent_tiles = get_adjacent_basin(tile[0], tile[1], inputs)
                        new_tiles += adjacent_tiles
                        basin += adjacent_tiles

                    tiles_to_check = new_tiles

                basin_sizes.append(len(basin))

    sorted_basin = sorted(basin_sizes, reverse=True)
    print("Result:", sorted_basin[0] * sorted_basin[1] * sorted_basin[2])


def get_adjacent_basin(i, j, tiles):
    adjacent_tiles = []

    if i != 0 and tiles[i - 1][j] not in [9, -1]:
        tiles[i - 1][j] = -1
        adjacent_tiles.append((i - 1, j))

    if j != 0 and tiles[i][j - 1] not in [9, -1]:
        tiles[i][j - 1] = -1
        adjacent_tiles.append((i, j - 1))

    if i < len(tiles) - 1 and tiles[i + 1][j] not in [9, -1]:
        tiles[i + 1][j] = -1
        adjacent_tiles.append((i + 1, j))

    if j < len(tiles[i]) - 1 and tiles[i][j + 1] not in [9, -1]:
        tiles[i][j + 1] = -1
        adjacent_tiles.append((i, j + 1))

    return adjacent_tiles


def main():
    file = open("input.txt", "r")
    inputs = [[int(character) for character in line]
              for line in file.read().split('\n')]

    part_one(inputs)
    part_two(inputs)


if __name__ == "__main__":
    main()
