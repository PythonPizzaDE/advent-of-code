from enum import Enum, auto

class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

def parse_shapes(guide: str) -> list[tuple[Shape]]:
    games = []
    for line in guide.split('\n'):
        primitive = line.split(' ')
        first = None
        second = None
        match primitive:
            case ['A', _]:
                first = Shape.ROCK
            case ['B', _]:
                first = Shape.PAPER
            case ['C', _]:
                first = Shape.SCISSORS

        match primitive:
            case [_, 'X']:
                second = Shape.ROCK
            case [_, 'Y']:
                second = Shape.PAPER
            case [_, 'Z']:
                second = Shape.SCISSORS
        games.append((first, second))
    return games

shape_scores = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}

def calculate_scores(games: list[tuple[Shape]]) -> int:
    scores = []
    for game in games:
        match game:
            # enemy plays rock
            case (Shape.ROCK, Shape.ROCK):
                scores.append(shape_scores[Shape.ROCK] + 3)
            case (Shape.ROCK, Shape.PAPER):
                scores.append(shape_scores[Shape.PAPER] + 6)
            case (Shape.ROCK, Shape.SCISSORS):
                scores.append(shape_scores[Shape.SCISSORS] + 0)

            # enemy plays paper
            case (Shape.PAPER, Shape.ROCK):
                scores.append(shape_scores[Shape.ROCK] + 0)
            case (Shape.PAPER, Shape.PAPER):
                scores.append(shape_scores[Shape.PAPER] + 3)
            case (Shape.PAPER, Shape.SCISSORS):
                scores.append(shape_scores[Shape.SCISSORS] + 6)

            # enemy plays scissors
            case (Shape.SCISSORS, Shape.ROCK):
                scores.append(shape_scores[Shape.ROCK] + 6)
            case (Shape.SCISSORS, Shape.PAPER):
                scores.append(shape_scores[Shape.PAPER] + 0)
            case (Shape.SCISSORS, Shape.SCISSORS):
                scores.append(shape_scores[Shape.SCISSORS] + 3)
            # otherwhise
            case _:
                print(game)
                print('something could be broken')
    return scores

with open('input.txt') as file:
    games = parse_shapes(file.read())

print(sum(calculate_scores(games)))
