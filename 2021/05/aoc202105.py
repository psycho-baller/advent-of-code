"""AoC 5, 2021"""

# Standard library imports
import pathlib
import sys
import numpy as np
import re


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def main(data, find_diagonals=True):
    # finds the largest number from the input
    x_size = int(max(x.strip(',')
                 for x in re.findall('\d+,', data))) + 1
    y_size = int(max(y.strip(',')
                 for y in re.findall(',\d+', data))) + 1
    # makes a 2D matrix with a size of *largest x coord* x *largest y coord*
    matrix = np.zeros((x_size, y_size))
    for line in data.splitlines():
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if (x1 == x2):
            x = x1
            for y in range(min(y2, y1), max(y2, y1)+1):
                matrix[x][y] += 1
        elif (y1 == y2):
            y = y1
            for x in range(min(x2, x1), max(x2, x1)+1):
                matrix[x][y] += 1
        elif find_diagonals:
            length = abs(x1 - x2)
            dx = (x2 - x1) / length
            dy = (y2 - y1) / length
            for n in range(length + 1):
                x = int(x1 + (dx * n))
                y = int(y1 + (dy * n))
                matrix[x][y] += 1

    return len([v for v in matrix.flatten() if v >= 2])


def part1(data):
    """Solve part 1"""
    return main(data, find_diagonals=False)


def part2(data):
    """Solve part 2"""
    return main(data)


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
