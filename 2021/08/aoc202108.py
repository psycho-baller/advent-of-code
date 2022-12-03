"""AoC 8, 2021"""

# Standard library imports
import pathlib
import sys


def parse(path, puzzle_input):
    """Parse input"""
    if path == 'example1.txt':
        puzzle_input = puzzle_input.replace('|\n', '|')
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1"""
    count = 0
    for line in data:
        _, output = line.split('|')
        parts = output.split()
        for part in parts:
            if len(part) in {2, 3, 4, 7}:
                count += 1
    return count


def part2(data):
    """Solve part 2"""
    return 'TODO'


def solve(path, puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(path, puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:

        print(f"\n{path}:")
        solutions = solve(path, puzzle_input=pathlib.Path(
            path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
