"""AoC 7, 2021"""

# Standard library imports
import pathlib
import sys
import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return np.array([int(x) for x in puzzle_input.strip().split(',')])


def part1(data):
    """Solve part 1"""
    fuel = {}
    # finds the Quartiles of the position of the crabs
    Q1, Q3 = np.percentile(data, [25, 75], interpolation='midpoint')
    Q1, Q3 = int(Q1), int(Q3)
    for pos in range(Q1, Q3+1):
        not_fuel = []
        for crab in data:
            not_fuel.append(abs(crab-pos))
        # adds each sum of fuel used to a dict with its 'value' as position of the horizontal
        fuel[pos] = sum(not_fuel)
    # finds the lowest key(fuel used) in the dict
    return fuel[min(fuel, key=fuel.get)]


def part2(data):
    """Solve part 2"""
    fuel = {}
    # finds the Quartiles of the position of the crabs
    Q1, Q3 = np.percentile(data, [25, 75], interpolation='midpoint')
    Q1, Q3 = int(Q1), int(Q3)
    for pos in range(Q1, Q3+1):
        not_fuel = []
        for crab in data:
            d = abs(crab-pos)  # distance needed to reach horisontal
            triangle_number = d*(d-1)/2  # extra rate need for each step
            fuel_needed = int(d + triangle_number)
            not_fuel.append(fuel_needed)
        # adds each sum of fuel used to a dict with its 'value' as position of the horizontal
        fuel[pos] = sum(not_fuel)
    # finds the lowest key(fuel used) in the dict
    return fuel[min(fuel, key=fuel.get)]


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
