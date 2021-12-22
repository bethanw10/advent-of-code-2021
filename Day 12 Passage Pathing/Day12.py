class Cave:
    def __init__(self, name: str, is_small: bool):
        self.name = name
        self.is_small = is_small
        self.connected_caves = set()

    def __repr__(self):
        return str(self.name)  # + " -> " + str([cave.name for cave in self.connected_caves])


def part_one(inputs):
    cave_system = parse_cave_system(inputs)

    start_cave = cave_system['start']
    path = [start_cave]
    complete_paths = []

    continue_path(path, complete_paths)

    print("Paths:", len(complete_paths))


def part_two(inputs):
    cave_system = parse_cave_system(inputs)

    start_cave = cave_system['start']
    path = [start_cave]
    complete_paths = []

    continue_path_part_2(path, complete_paths)

    print("Paths:", len(complete_paths))


def parse_cave_system(paths):
    cave_system = {}

    for path in paths:
        cave_a_name, cave_b_name = path.split('-')

        if cave_a_name not in cave_system:
            cave_a = Cave(cave_a_name, str.islower(cave_a_name))
            cave_system[cave_a_name] = cave_a
        else:
            cave_a = cave_system[cave_a_name]

        if cave_b_name not in cave_system:
            cave_b = Cave(cave_b_name, str.islower(cave_b_name))
            cave_system[cave_b_name] = cave_b
        else:
            cave_b = cave_system[cave_b_name]

        cave_a.connected_caves.add(cave_b)
        cave_b.connected_caves.add(cave_a)

    return cave_system


def continue_path(path, complete_paths):
    current_cave = path[-1]

    available_caves = [cave for cave in current_cave.connected_caves
                       if (not cave.is_small or cave not in path)]

    for cave in available_caves:
        new_path = path.copy()
        new_path.append(cave)

        if cave.name == 'end':
            complete_paths.append(new_path)
        else:
            continue_path(new_path, complete_paths)


def continue_path_part_2(path, complete_paths, visited_twice=False):
    current_cave = path[-1]

    visits_allowed = 0 if visited_twice else 1

    available_caves = [cave for cave in current_cave.connected_caves
                       if cave.name != "start" and (not cave.is_small or path.count(cave) <= visits_allowed)]

    for cave in available_caves:
        new_path = path.copy()
        new_path.append(cave)

        new_path_visited_twice = visited_twice or (cave.is_small and cave in path)

        if cave.name == 'end':
            complete_paths.append(new_path)
        else:
            continue_path_part_2(new_path, complete_paths, new_path_visited_twice)


def main():
    file = open("input.txt", "r")
    inputs = file.read().split('\n')

    part_one(inputs)
    part_two(inputs)


if __name__ == "__main__":
    main()
