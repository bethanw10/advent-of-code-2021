import statistics
import sys


def part_one(inputs):
    positions = list(map(int, inputs))

    median = statistics.median(positions)

    fuel = 0

    for position in positions:
        fuel += abs(position - median)

    print(fuel)


def part_two(inputs):
    positions = sorted(list(map(int, inputs)))

    lowest_fuel = sys.maxsize

    for i in range(positions[0], positions[len(positions) - 1]):
        total_fuel = 0
        for pos in positions:
            dist = abs(pos - i)
            total_fuel += (dist * (dist+1))/2

        if total_fuel < lowest_fuel:
            lowest_fuel = total_fuel

    print(lowest_fuel)


def main():
    file = open("input.txt", "r")
    inputs = file.read().split(',')

    part_one(inputs)
    part_two(inputs)


if __name__ == "__main__":
    main()
