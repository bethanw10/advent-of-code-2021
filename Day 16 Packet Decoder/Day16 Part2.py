LITERAL_ID = 4


def multiply(numbers):
    a = 1
    for num in numbers:
        a *= num
    return a


def part_two(value):
    hexadecimal = int(value, 16)
    packets = format(hexadecimal, "040b").rjust(len(value) * 4, "0")

    result, _ = process_packets(packets)
    print("Result:", result)


def process_packets(packets):
    type_id = int(packets[3:6], 2)

    if type_id != LITERAL_ID:  # then packet is operator
        numbers, end_index = process_operator_packet(packets)

        if type_id == 0:
            result = sum(numbers)
        elif type_id == 1:
            result = multiply(numbers)
        elif type_id == 2:
            result = min(numbers)
        elif type_id == 3:
            result = max(numbers)
        elif type_id == 5:
            result = int(numbers[0] > numbers[1])
        elif type_id == 6:
            result = int(numbers[0] < numbers[1])
        elif type_id == 7:
            result = int(numbers[0] == numbers[1])
        else:
            raise Exception("Type id not expected")
    else:
        result, end_index = process_literal_packet(packets)

    return result, end_index


def process_operator_packet(packets):
    all_numbers = []
    length_id = packets[6]

    if length_id == '0':
        length = 15

        total_sub_packet_length = int(packets[7: 7 + length], 2)
        current_index = 7 + length
        end_sub_packets_index = 7 + length + total_sub_packet_length
        sub_packets = packets[current_index: end_sub_packets_index]

        while sub_packets != '':
            result, packet_length = process_packets(sub_packets)
            current_index += packet_length
            all_numbers.append(result)

            sub_packets = packets[current_index: end_sub_packets_index]
    else:
        length = 11
        num_sub_packets = int(packets[7: 7 + length], 2)
        current_index = 0

        for i in range(num_sub_packets):
            sub_packets = packets[7 + length + current_index:]

            result, packet_length = process_packets(sub_packets)
            all_numbers.append(result)
            current_index += packet_length

        end_sub_packets_index = 7 + length + current_index

    return all_numbers, end_sub_packets_index


def process_literal_packet(packets):
    number = ''
    group_prefix = '1'
    i = 6

    while group_prefix != '0':
        group_prefix = packets[i:i + 1]
        digit = packets[i + 1: i + 5]
        number += digit
        i += 5

    number = int(number, 2)

    return number, i


def main():
    file = open("input.txt", "r")
    value = file.read()

    part_two(value)


if __name__ == "__main__":
    main()
