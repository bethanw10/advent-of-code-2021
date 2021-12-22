from itertools import combinations
from math import sqrt

SCANNER_RANGE = 1000

class Distance:
    def __init__(self, point_a, point_b, distance):
        self.point_a = point_a
        self.point_b = point_b
        self.distance = distance


def part_one(scanner_list):
    scanners = {}

    for scanner in scanner_list:
        name = scanner[0]
        points = [tuple([int(p) for p in point.split(',')])
                  for point in scanner[1:]]

        scanners[name] = points

    scanner_combos = combinations(scanners, 2)

    for scanner1, scanner2 in scanner_combos:
        # pre calc
        dists1 = get_distances(scanners[scanner1])
        dists2 = get_distances(scanners[scanner2])

        for p1, p2 in [(a, b) for a in dists1 for b in dists2]:
            p1_dists = dists1[p1]
            p2_dists = dists2[p2]

            p1_dists, p2_dists = filter_out_of_range(p1, p1_dists, p2, p2_dists)

            potential_match = True

            if len(p1_dists) != len(p2_dists) or len(p1_dists) == 0:
                potential_match = False
            else:
                for connected_point, dist1 in p1_dists:
                    matching_dist = [connected_point for connected_point, dist2 in p2_dists if dist1 == dist2]

                    if len(matching_dist) == 0:
                        potential_match = False

                    if len(matching_dist) > 1:
                        print("huh?")

            if potential_match:
                print(p1, p1_dists)
                print(p2, p2_dists)
                print()


def get_distances(points):
    dists = {p: [] for p in points}

    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue

            dists[p1].append(distance(p1, p2))

    return dists


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]

    return int(sqrt(dx * dx + dy * dy + dz * dz))

# Filters out connections to other beacons if they would be out of range of the other scanner
# (if they ARE the same points)
def filter_out_of_range(p1, p1_dists, p2, p2_dists):
    filtered_p1_dists = []

    for connected_point, dist1 in p1_dists:
        in_range = True
        for dim in range(3):
            scanner_2_dist = abs(p2[dim] + dist1[dim])

            if scanner_2_dist > 1000:
                in_range = False
                break

        if in_range:
            filtered_p1_dists.append((connected_point, dist1))

    filtered_p2_dists = []

    for connected_point, dist2 in p2_dists:
        in_range = True
        for dim in range(3):
            scanner_1_dist = abs(p1[dim] + dist2[dim])

            if scanner_1_dist > 1000:
                in_range = False
                break

        if in_range:
            filtered_p2_dists.append((connected_point, dist2))

    return filtered_p1_dists, filtered_p2_dists


def get_relative_distances(points):
    dists = {p: [] for p in points}

    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue

            dists[p1].append(
                (p2,
                 (p1[0] - p2[0],
                  p1[1] - p2[1],
                  p1[2] - p2[2]))
            )

    return dists


def part_two(scanners):
    pass


def main():
    scanners = [scanner.split('\n') for scanner in
                open("input.txt", "r").read().split('\n\n')]

    part_one(scanners)
    part_two(scanners)


if __name__ == "__main__":
    main()
