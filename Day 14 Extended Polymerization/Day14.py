import math


def part_one(polymer, rules):
    for step in range(10):
        new_polymer = ''
        for i in range(len(polymer) - 1):
            pair = polymer[i:i + 2]
            new_polymer += polymer[i]

            if pair in rules:
                new_polymer += rules[pair]

        new_polymer += polymer[-1]
        polymer = new_polymer

    element_counts = {polymer[i]: polymer.count(polymer[i]) for i in range(len(polymer))}
    most_common_el = max(element_counts, key=element_counts.get)
    least_common_el = min(element_counts, key=element_counts.get)
    print("Difference:", element_counts[most_common_el] - element_counts[least_common_el])


def part_two(polymer, rules):
    polymer = {polymer[i:i + 2]: polymer.count(polymer[i:i + 2])
               for i in range(len(polymer) - 1)}

    for step in range(40):
        new_polymer = {}

        for pair, count in polymer.items():
            if pair in rules:
                element = rules[pair]

                left_pair = pair[0] + element
                right_pair = element + pair[1]

                new_polymer[left_pair] = new_polymer.get(left_pair, 0) + count
                new_polymer[right_pair] = new_polymer.get(right_pair, 0) + count
            else:
                new_polymer[pair] = count

        polymer = new_polymer

    element_counts = {}
    for pair, count in polymer.items():
        element_counts[pair[0]] = element_counts.get(pair[0], 0) + count
        element_counts[pair[1]] = element_counts.get(pair[1], 0) + count

    most_common_el = max(element_counts, key=element_counts.get)
    least_common_el = min(element_counts, key=element_counts.get)
    difference = element_counts[most_common_el] - element_counts[least_common_el]

    print("Difference:", math.ceil(difference/2))


def main():
    file = open("input.txt", "r")
    template, rules = file.read().split('\n\n')
    rules = dict([rule.split(" -> ") for rule in rules.split('\n')])

    part_one(template, rules)
    part_two(template, rules)


if __name__ == "__main__":
    main()
