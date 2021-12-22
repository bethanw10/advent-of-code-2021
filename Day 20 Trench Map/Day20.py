DIRECTIONS = [(dx, dy) for dy in [-1, 0, 1] for dx in [-1, 0, 1]]


def enhance(algorithm, image, steps):
    infinite_pixel = '0'

    for step in range(steps):
        min_x = min(image, key=lambda k: k[0])[0]
        min_y = min(image, key=lambda k: k[1])[1]

        max_x = max(image, key=lambda k: k[0])[0]
        max_y = max(image, key=lambda k: k[1])[1]

        new_image = {}

        for y in range(min_x - 2, max_y + 2):
            for x in range(min_y - 2, max_x + 2):
                number = ''

                for dx, dy in DIRECTIONS:
                    current_x, current_y = x + dx, y + dy

                    if (current_x, current_y) in image:
                        pixel = image[(current_x, current_y)]
                        number += pixel_to_bit(pixel)
                    else:
                        number += infinite_pixel

                number = int(number, 2)
                new_pixel = algorithm[number]
                new_image[(x, y)] = new_pixel

        image = new_image
        infinite_pixel_index = int(infinite_pixel*9, 2)
        infinite_pixel = pixel_to_bit(algorithm[infinite_pixel_index])

        # print_grid(new_image, infinite_pixel)
        # print()

    # print_grid(image)

    print("Num dark pixels:", len([pixel for _, pixel in image.items() if pixel == '#']))


def pixel_to_bit(pixel):
    return '0' if pixel == '.' else '1'


def print_grid(grid, default='0'):
    default_char = '.' if default == '0' else '#'

    min_x = min(grid, key=lambda k: k[0])[0]
    min_y = min(grid, key=lambda k: k[1])[1]

    max_x = max(grid, key=lambda k: k[0])[0]
    max_y = max(grid, key=lambda k: k[1])[1]

    for y in range(min_y - 2, max_y + 2):
        for x in range(min_x - 2, max_x + 2):
            if (x, y) in grid:
                print(grid[(x, y)], end='')
            else:
                print(f'\033[90m{default_char}\033[0m', end='')
        print()


def main():
    algorithm, image = open("input.txt", "r").read().split('\n\n')
    image = [[pixel for pixel in line] for line in image.split('\n')]

    image_dict = {}

    for y, line in enumerate(image):
        for x, pixel in enumerate(line):
            image_dict[(x, y)] = pixel

    enhance(algorithm, image_dict, 2)
    enhance(algorithm, image_dict, 50)


if __name__ == "__main__":
    main()
