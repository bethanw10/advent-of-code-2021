from collections import defaultdict

from parse import parse


def part_one(instructions):
    cubes = defaultdict(bool)

    for instruction in instructions:
        state, area = instruction.split(' ')
        x, y, z = area.split(',')

        min_x, max_x = parse('x={:d}..{:d}', x)
        min_y, max_y = parse('y={:d}..{:d}', y)
        min_z, max_z = parse('z={:d}..{:d}', z)

        if any(n > 50 for n in [min_x, max_x, min_y, max_y, min_z, max_z]) or \
                any(n < -50 for n in [min_x, max_x, min_y, max_y, min_z, max_z]):
            continue

        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    cubes[(x, y, z)] = (state == 'on')

        # print_grid(cubes)

    print(len([cube for cube, state in cubes.items() if state]))


def print_grid(grid):
    min_x = min(grid, key=lambda k: k[0])[0]
    min_y = min(grid, key=lambda k: k[1])[1]
    min_z = min(grid, key=lambda k: k[2])[2]

    max_x = max(grid, key=lambda k: k[0])[0]
    max_y = max(grid, key=lambda k: k[1])[1]
    max_z = max(grid, key=lambda k: k[2])[2]

    for z in range(min_z, max_z + 1):
        print("z =", z)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y, z) in grid:
                    print(int(grid[(x, y, z)]), end='')
                else:
                    print(f'\033[90m0\033[0m', end='')
            print()
        print('\n')


class Cuboid:
    def __init__(self, x_range, y_range, z_range):
        self.x1, self.x2 = x_range
        self.y1, self.y2 = y_range
        self.z1, self.z2 = z_range
        self.subtractions = []

    def intersect(self, cube):
        x1, x2 = max(self.x1, cube.x1), min(self.x2, cube.x2)
        y1, y2 = max(self.y1, cube.y1), min(self.y2, cube.y2)
        z1, z2 = max(self.z1, cube.z1), min(self.z2, cube.z2)

        if x1 > x2 or y1 > y2 or z1 > z2:
            return

        overlap = Cuboid((x1, x2), (y1, y2), (z1, z2))

        for sub in self.subtractions:
            overlap.intersect(sub)

        if overlap.area() > 0:
            self.subtractions.append(overlap)

    @property
    def area_before_subtractions(self):
        return (abs(self.x2 - self.x1)) * (abs(self.y2 - self.y1)) * (abs(self.z2 - self.z1))

    def area(self):
        main_area = self.area_before_subtractions

        for sub in self.subtractions:
            sub_area = sub.area()
            main_area -= sub_area

        return max(main_area, 0)

    def __repr__(self):
        return f'x:{self.x1}..{self.x2}  y:{self.y1}..{self.y2}  z:{self.z1}..{self.z2} ({self.area()})'


def part_two(instructions):
    cube_regions = []

    for instruction in instructions:
        state, area = instruction.split(' ')
        x, y, z = area.split(',')

        min_x, max_x = parse('x={:d}..{:d}', x)
        min_y, max_y = parse('y={:d}..{:d}', y)
        min_z, max_z = parse('z={:d}..{:d}', z)

        new_cube = Cuboid((min_x, max_x + 1), (min_y, max_y + 1), (min_z, max_z + 1))

        for cube in cube_regions:
            cube.intersect(new_cube)

        if state == 'on':
            cube_regions.append(new_cube)

    print(sum([cube.area() for cube in cube_regions]))


def main():
    instructions = open("input.txt", "r").read().split('\n')

    part_one(instructions)
    part_two(instructions)


if __name__ == "__main__":
    main()
