"""AoC 1, 2021"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def part2(data):
    """Solve part 2"""
    return sum(data[i] > data[i - 3] for i in range(3, len(data)))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
