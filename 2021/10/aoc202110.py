"""AoC 10, 2021"""

# Standard library imports
import pathlib
import sys
import numpy as np
from numpy.lib.function_base import median


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1"""
    POINTS = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    OPENING = {'{': '}', '(': ')', '[': ']', '<': '>'}
    CLOSING = {v: k for k, v in OPENING.items()}
    total = 0
    for line in data:
        stack = []
        for i in line:
            if i in OPENING:
                stack.append(i)
            elif i in CLOSING:
                if CLOSING[i] == stack[-1]:
                    stack.pop()
                else:
                    total += POINTS[i]
                    break
    return total


def part2(data):
    """Solve part 2"""
    POINTS = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    POINTS2 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    OPENING = {'{': '}', '(': ')', '[': ']', '<': '>'}
    CLOSING = {v: k for k, v in OPENING.items()}
    answer = []
    for line in data:
        stack = []
        for i in line:
            if i in OPENING:
                stack.append(i)
            elif i in CLOSING:
                if CLOSING[i] == stack[-1]:
                    stack.pop()
                else:
                    break
        else:
            sum = 0
            for i in reversed(stack):  # -1, -1, -1):
                sum *= 5
                sum += POINTS2[i]
            answer.append(sum)
    return int(median(answer))


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
