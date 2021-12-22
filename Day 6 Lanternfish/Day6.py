def part_one(inputs):
    fish_timers = list(map(int, inputs))

    for day in range(80):
        new_fish = []

        for i in range(len(fish_timers)):
            fish_timer = fish_timers[i]
            fish_timers[i] -= 1

            if fish_timer == 0:
                new_fish.append(8)
                fish_timers[i] = 6

        fish_timers += new_fish

    print("Number of fish:", len(fish_timers))


def part_two(lines):
    fish_timers = {int(fish): lines.count(fish) for fish in lines}

    for day in range(256):
        new_fish_timers = {i: 0 for i in range(9)}

        for fish_timer, count in fish_timers.items():
            if fish_timer == 0:
                new_fish_timers[8] = count
                new_fish_timers[6] = count
            else:
                new_fish_timers[fish_timer - 1] += count

        fish_timers = new_fish_timers

    print("Number of fish:", sum(fish_timers.values()))


def main():
    file = open("input.txt", "r")
    inputs = file.read().split(',')

    part_one(inputs)
    part_two(inputs)


if __name__ == "__main__":
    main()
