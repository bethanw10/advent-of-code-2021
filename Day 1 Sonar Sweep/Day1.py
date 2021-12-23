def part_one(numbers):
    prev_number = numbers[0]
    num_increases = 0

    for number in numbers[1:]:
        if number > prev_number:
            num_increases += 1

        prev_number = number

    print("Number of increases:", num_increases)


def part_two(numbers):
    previous_window = sum(numbers[0:3])
    num_increases = 0

    for index in range(3, len(numbers)):
        window = sum(numbers[index - 2: index + 1])

        if window > previous_window:
            num_increases += 1

        previous_window = window

    print("Number of window increases:", num_increases)


def main():
    file = open("input.txt", "r")
    lines = file.read().split('\n')
    numbers = [int(n) for n in lines if n.strip()]

    part_one(numbers)
    part_two(numbers)


if __name__ == "__main__":
    main()

