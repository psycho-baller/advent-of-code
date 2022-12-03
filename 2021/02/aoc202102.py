"""AoC 2, 2021"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    position = depth = 0
    for i in data.splitlines():
        direction, count = i.split()
        count = int(count)
        if direction == 'forward':
            position += count
        elif direction == 'up':
            depth -= count
        else:
            depth += count
    return position * depth


def part2(data):
    """Solve part 2"""
    position = depth = aim = 0
    for i in data.splitlines():
        direction, count = i.split()
        count = int(count)
        if direction == 'down':
            aim += count
        elif direction == 'up':
            aim -= count
        else:
            position += count
            depth += count*aim
    return position * depth


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
