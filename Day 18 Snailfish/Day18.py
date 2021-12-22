import math
from typing import List


class SnailfishElement:
    def __init__(self, value, nest_level):
        self.nest_level = nest_level
        self.value = value

    def __repr__(self):
        return str(self.value)


class SnailfishNumber:
    elems: List[SnailfishElement]

    def __init__(self, children):
        self.elems = []

        self.parse_array(children)

    def parse_array(self, arr, current_level=1):
        for el in arr:
            if type(el) is int:
                self.elems.append(SnailfishElement(el, current_level))
            else:
                self.parse_array(el, current_level + 1)

    def add(self, number):
        self.elems += number.elems

        for el in self.elems:
            el.nest_level += 1

        self.reduce()

    def reduce(self):
        action_occurred = True

        while action_occurred:
            action_occurred = False

            if self.explode():
                # print('Explode')
                # print(self)
                action_occurred = True

            elif self.split():
                # print('Split')
                # print(self)
                action_occurred = True

    def explode(self):
        for i, left_el in enumerate(self.elems[:-1]):
            right_el = self.elems[i + 1]
            if 5 <= left_el.nest_level == right_el.nest_level:
                if i != 0:
                    self.elems[i - 1].value += left_el.value

                if i + 2 < len(self.elems):
                    self.elems[i + 2].value += right_el.value

                self.elems[i:i + 2] = [SnailfishElement(0, left_el.nest_level - 1)]

                return True
        return False

    def split(self):
        for i, el in enumerate(self.elems):
            if el.value >= 10:
                left = math.floor(el.value / 2)
                right = math.ceil(el.value / 2)

                self.elems[i:i + 1] = [SnailfishElement(left, el.nest_level + 1),
                                       SnailfishElement(right, el.nest_level + 1)]

                return True
        return False

    def magnitude(self):
        elems = self.elems.copy()

        while len(elems) != 1:
            for i, left_el in enumerate(elems[:-1]):
                right_el = elems[i + 1]
                if left_el.nest_level == right_el.nest_level:
                    magnitude = (3 * left_el.value) + (2 * right_el.value)
                    elems[i:i + 2] = [SnailfishElement(magnitude, left_el.nest_level-1)]
                    break

        return elems[0].value

    def __repr__(self):
        return ', '.join([str(el) for el in self.elems]) + ' (numbers)'\
               '\n\033[90m' + ', '.join([str(el.nest_level) for el in self.elems]) + '\033[0m (nest levels)\n'


def part_one(numbers):
    total = SnailfishNumber(numbers[0])

    for number in numbers[1:]:
        total.add(SnailfishNumber(number))

    print(total.magnitude())


def part_two(numbers):
    highest_magnitude = 0

    for num1 in numbers:
        for num2 in numbers:
            sf_num1 = SnailfishNumber(num1)
            sf_num2 = SnailfishNumber(num2)

            sf_num1.add(sf_num2)
            magnitude = sf_num1.magnitude()

            if magnitude > highest_magnitude:
                highest_magnitude = magnitude

    print(highest_magnitude)


def main():
    numbers = [eval(number) for number in open("input.txt", "r").read().split('\n')]

    part_one(numbers)
    part_two(numbers)


if __name__ == "__main__":
    main()
