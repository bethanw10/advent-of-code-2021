def part_one(numbers):
    number_length = len(numbers[0])
    gamma = ''
    epsilon = ''

    for i in range(number_length):
        count_1, count_0 = get_bit_counts(numbers, i)

        if count_1 > count_0:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    gamma_bin = int(gamma, 2)
    epsilon_bin = int(epsilon, 2)

    print("Gamma:", gamma_bin)
    print("Epsilon:", epsilon_bin)
    print("Result:", gamma_bin * epsilon_bin)


def part_two(numbers):
    number_length = len(numbers[0])

    oxygen_ratings = numbers.copy()
    co2_ratings = numbers.copy()

    for i in range(number_length):
        if len(oxygen_ratings) != 1:
            count_1, count_0 = get_bit_counts(oxygen_ratings, i)
            most_common = '1' if count_1 >= count_0 else '0'
            oxygen_ratings = [o for o in oxygen_ratings if o[i] == most_common]

        if len(co2_ratings) != 1:
            count_1, count_0 = get_bit_counts(co2_ratings, i)
            least_common = '0' if count_1 >= count_0 else '1'
            co2_ratings = [c for c in co2_ratings if c[i] == least_common]

    oxygen_rating = int(oxygen_ratings[0], 2)
    co2_rating = int(co2_ratings[0], 2)

    print("O2:", oxygen_ratings, oxygen_rating)
    print("CO2:", co2_ratings, co2_rating)
    print("Result:", co2_rating * oxygen_rating)


def get_bit_counts(numbers, i):
    count_1, count_0 = 0, 0

    for num in numbers:
        if num[i] == '1':
            count_1 += 1
        else:
            count_0 += 1

    return count_1, count_0


def main():
    file = open("input.txt", "r")
    lines = file.read().split('\n')

    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()

