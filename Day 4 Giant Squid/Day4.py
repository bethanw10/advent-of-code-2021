class BingoSquare:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def __repr__(self):
        if self.marked:
            return str(self.number) + "*"
        else:
            return str(self.number) + " "


def get_winning_board(numbers, boards):
    for num in numbers:
        for board in boards:
            for row in board:
                for square in row:
                    if square.number == num:
                        square.marked = True

            if check_win(board):
                return board, num


def check_win(board):
    for row in board:
        full_row = True

        for square in row:
            if not square.marked:
                full_row = False
                break

        if full_row:
            return True

    for i in range(0, len(board[0])):
        full_column = True
        for row in board:
            if not row[i].marked:
                full_column = False
                break

        if full_column:
            return True


def get_losing_board(numbers, boards):
    not_won = boards.copy()

    for num in numbers:
        for board in boards:
            if board not in not_won:
                continue

            for row in board:
                for square in row:
                    if square.number == num:
                        square.marked = True

            if check_win(board):
                if len(not_won) == 1:
                    return not_won[0], num
                else:
                    not_won.remove(board)


def calculate_score(number, board):
    unmarked_total = 0

    for row in board:
        for square in row:
            if not square.marked:
                unmarked_total += int(square.number)

    return unmarked_total * int(number)


def part_one(numbers, boards):
    winning_board, winning_number = get_winning_board(numbers, boards)

    print("Winning board score:", calculate_score(winning_number, winning_board))


def part_two(numbers, boards):
    losing_board, last_number = get_losing_board(numbers, boards)

    print("Losing board score:", calculate_score(last_number, losing_board))


def main():
    file = open("input.txt", "r")
    bingo = file.read().split('\n\n')

    numbers = bingo[0].split(',')
    boards_string = bingo[1:]
    boards = []

    for board in boards_string:
        board = [[BingoSquare(square) for square in row.split(" ") if square]
                 for row in board.split('\n')]

        boards.append(board)

    part_one(numbers, boards)
    part_two(numbers, boards)


if __name__ == "__main__":
    main()
