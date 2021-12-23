#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


def part_one(inputs):
    total_1_4_7_8 = 0

    for sequence in inputs:
        for digit in sequence[1].split():
            if len(digit) in [2, 4, 3, 7]:
                total_1_4_7_8 += 1

    print("Total 1, 4, 7, or 8:", total_1_4_7_8)


def part_two(inputs):
    digit_segments = {
        '0': ['a', 'b', 'c', 'e', 'f', 'g'],
        '1': ['c', 'f'],
        '2': ['a', 'c', 'd', 'e', 'g'],
        '3': ['a', 'c', 'd', 'f', 'g'],
        '4': ['b', 'c', 'd', 'f'],
        '5': ['a', 'b', 'd', 'f', 'g'],
        '6': ['a', 'b', 'd', 'e', 'f', 'g'],
        '7': ['a', 'c', 'f'],
        '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        '9': ['a', 'b', 'c', 'd', 'f', 'g']
    }

    segments = set('abcdefg')

    total_output = 0

    for sequence in inputs:
        pattern, output = sequence

        wire_map = {letter: segments.copy() for letter in segments}

        pattern_digits = pattern.split()
        pattern_digits_by_len = {}

        # Build dictionary of pattern digits to number of wires
        for pattern_digit in pattern_digits:
            length = len(pattern_digit)

            if length not in pattern_digits_by_len:
                pattern_digits_by_len[length] = []

            pattern_digits_by_len[length].append(pattern_digit)

        # Calculate wire mappings
        for length, pattern_digits in pattern_digits_by_len.items():
            same_length_digits = [v for d, v in digit_segments.items() if len(v) == length]

            shared_segments = set(same_length_digits[0]).intersection(*same_length_digits[1:])
            shared_digit_letters = set(pattern_digits[0]).intersection(*pattern_digits[1:])

            for wire, mappings in wire_map.items():
                if wire in shared_digit_letters:
                    wire_map[wire].intersection_update(shared_segments)
                else:
                    wire_map[wire].difference_update(shared_segments)

        # Translate output using mapping
        output_number = ''
        for digit in output.split():
            actual_wires = ''

            for wire in digit:
                if len(wire_map[wire]) != 1:
                    raise Exception("Mapping failed")

                actual_wire, *_ = wire_map[wire]
                actual_wires += actual_wire

            mapped_digit = next(d for d, wires in digit_segments.items() if set(wires) == set(actual_wires))

            output_number += mapped_digit

        total_output += int(output_number)

    print("Total output:", total_output)


def main():
    file = open("input.txt", "r")
    inputs = [digit.split('|') for digit in file.read().split('\n')]

    part_one(inputs)
    part_two(inputs)


if __name__ == "__main__":
    main()
