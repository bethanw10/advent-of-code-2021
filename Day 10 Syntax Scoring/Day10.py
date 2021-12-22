bracket_map = {
    ')': '(', ']': '[', '}': '{', '>': '<'
}

reverse_bracket_map = {bracket_map[key]: key for key in bracket_map.keys()}


def part_one(inputs):
    bracket_scores = {
        ')': 3, ']': 57, '}': 1197, '>': 25137
    }

    total = 0

    for line in inputs:
        bracket_stack = []
        invalid_brackets = []

        for bracket in line:
            if bracket not in bracket_map:
                bracket_stack.append(bracket)
            else:
                last_open_bracket = bracket_stack.pop()
                matching_close_bracket = bracket_map[bracket]

                if last_open_bracket != matching_close_bracket:
                    invalid_brackets.append(bracket)

        for invalid_bracket in invalid_brackets:
            score = bracket_scores[invalid_bracket]
            total += score

    print("Total score:", total)


def part_two(inputs):
    autocomplete_scores = {
        ')': 1, ']': 2, '}': 3, '>': 4
    }

    total_scores = []

    for line in inputs:
        bracket_stack = []

        for bracket in line:
            if bracket not in bracket_map:
                bracket_stack.append(bracket)
            else:
                last_open_bracket = bracket_stack.pop()
                matching_close_bracket = bracket_map[bracket]

                if last_open_bracket != matching_close_bracket:
                    bracket_stack = []
                    break

        if len(bracket_stack) != 0:
            score = 0
            while len(bracket_stack) != 0:
                score *= 5
                next_bracket = bracket_stack.pop()
                close_bracket = reverse_bracket_map[next_bracket]
                bracket_score = autocomplete_scores[close_bracket]
                score += bracket_score

            total_scores.append(score)

    print("Middle score:", sorted(total_scores)[len(total_scores)//2])


def main():
    file = open("input.txt", "r")
    inputs = file.read().split('\n')

    part_one(inputs)
    part_two(inputs)


if __name__ == "__main__":
    main()
