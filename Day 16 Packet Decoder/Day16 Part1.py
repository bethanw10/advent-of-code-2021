LITERAL_ID = 4


def part_one(value):
    hexadecimal = int(value, 16)
    packets = format(hexadecimal, "040b").rjust(len(value) * 4, "0")

    total_versions, _, _ = process_packets(packets)
    print(total_versions)


def process_packets(packets):
    version = int(packets[0:3], 2)
    type_id = int(packets[3:6], 2)

    total_version = version

    if type_id != LITERAL_ID:  # then packet is operator
        version, numbers, end_index = process_operator_packet(packets)
        total_version += version
    else:
        numbers, end_index = process_literal_packet(packets)

    return total_version, numbers, end_index


def process_operator_packet(packets):
    total_version = 0
    all_numbers = []
    length_id = packets[6]

    if length_id == '0':
        length = 15

        total_sub_packet_length = int(packets[7: 7 + length], 2)
        current_index = 7 + length
        end_sub_packets_index = 7 + length + total_sub_packet_length
        sub_packets = packets[current_index: end_sub_packets_index]

        while sub_packets != '':
            version, numbers, packet_length = process_packets(sub_packets)
            total_version += version
            current_index += packet_length
            all_numbers += numbers
            sub_packets = packets[current_index: end_sub_packets_index]
    else:
        length = 11
        num_sub_packets = int(packets[7: 7 + length], 2)
        current_index = 0

        for i in range(num_sub_packets):
            sub_packets = packets[7 + length + current_index:]

            version, numbers, packet_length = process_packets(sub_packets)
            total_version += version
            all_numbers += numbers
            current_index += packet_length

        end_sub_packets_index = 7 + length + current_index

    return total_version, all_numbers, end_sub_packets_index


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

    return [number], i


def main():
    file = open("input.txt", "r")
    value = file.read()

    part_one(value)


if __name__ == "__main__":
    main()
