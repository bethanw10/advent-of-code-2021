def part_one(players):
    scores = run(players)
    print(scores)


def run(players):
    die = 1
    dice_rolls = 0

    scores = {0: 0, 1: 0}

    while True:
        for i in range(2):
            for d in range(3):
                players[i] += die
                die = die + 1 if die != 100 else 1

            dice_rolls += 3

            if players[i] > 10:
                players[i] %= 10
                if players[i] == 0:
                    players[i] = 10

            scores[i] += players[i]

            if scores[i] >= 1000:
                losing_score = scores[0] if i == 1 else scores[1]
                return losing_score * dice_rolls


class Game:
    def __init__(self, positions, scores, count):
        self.count = count
        self.scores = scores
        self.spaces = positions

    def copy(self):
        return Game(self.spaces.copy(), self.scores.copy(), self.count)


def run_quantum(players):
    die_outcomes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    games = [Game(players.copy(), {0: 0, 1: 0}, 1)]

    wins = {0: 0, 1: 0}

    turns = 0

    while len(games) > 0:
        turns += 1

        for i in range(2):
            new_games = []

            for game in games:
                for outcome, num_universes in die_outcomes.items():
                    new_game = game.copy()
                    new_game.spaces[i] += outcome

                    if new_game.spaces[i] > 10:
                        new_game.spaces[i] %= 10 or 10

                    new_game.scores[i] += new_game.spaces[i]
                    new_game.count *= num_universes

                    if new_game.scores[i] >= 21:
                        wins[i] += new_game.count
                    else:
                        new_games.append(new_game)

            games = new_games

    print(wins)


def part_two(players):
    run_quantum(players)


def main():
    player1, player2 = open("input.txt", "r").read().split('\n')

    players = {0: int(player1[-1]), 1: int(player2[-1])}

    part_one(players.copy())
    part_two(players.copy())


if __name__ == "__main__":
    main()
