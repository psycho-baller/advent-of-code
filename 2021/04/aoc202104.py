"""AoC 4, 2021"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    numbers, *boards = puzzle_input.split('\n\n')
    numbers = [int(num) for num in numbers.split(',')]

    boards = [[line.split() for line in board.split('\n')] for board in boards]
    boards = [[[int(elt) for elt in line] for line in board]
              for board in boards]
    return numbers, boards


class Board:
    def __init__(self, board):
        self.board = board
        self.row = len(self.board)
        self.col = len(self.board[0])
        self.found = [[False] * self.col for _ in range(self.row)]
        # ^ initializes each number in the board with a False, when found,
        # it'll be turned to True using the function make_found()
        self.last_num = None

    def make_found(self, number):
        self.last_num = number
        for r in range(self.row):
            for c in range(self.col):
                if self.board[r][c] == number:
                    self.found[r][c] = True

    def check_win(self):
        # goes through the selected board and checks if
        # there's at least 1 row/col where all values are True,
        # if yes then it'll return true
        return (any(all(row) for row in self.found) or
                any(all(col) for col in zip(*self.found)))
        # zip(*self.found) explanation:
        # https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist/29139418

    def sum_unmarked(self):
        sum_of_unmarked = 0
        for r in range(self.row):
            for c in range(self.col):
                if not self.found[r][c]:
                    sum_of_unmarked += int(self.board[r][c])
        return sum_of_unmarked


def find_winners(numbers, boards, part):
    boards = [Board(board) for board in boards]

    winners = []
    for number in numbers:
        for i in range(len(boards)-1, -1, -1):
            boards[i].make_found(number)
            if boards[i].check_win():
                winners.append(boards[i])
                boards.pop(i)
    if part == 1:
        return winners[0].sum_unmarked() * winners[0].last_num
    else:
        return winners[-1].sum_unmarked() * winners[-1].last_num


def part1(numbers, boards):
    """Solve part 1"""
    return find_winners(numbers, boards, part=1)


def part2(numbers, boards):
    """Solve part 2"""
    return find_winners(numbers, boards, part=2)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    numbers, boards = parse(puzzle_input)
    solution1 = part1(numbers, boards)
    solution2 = part2(numbers, boards)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
