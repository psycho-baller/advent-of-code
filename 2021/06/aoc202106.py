"""AoC 6, 2021"""

# Standard library imports
import pathlib
import sys
import collections


def parse(puzzle_input):
    """Parse input"""
    return collections.Counter(int(x) for x in puzzle_input.strip().split(','))


def main(data, days):
    for _ in range(days):
        # all 0's will turn to a 6 and an 8
        not_data = collections.Counter({6: data[0], 8: data[0]})
        # all numbers in the data greater than 0 will be reduced by 1
        not_data.update({time-1: counter for time,
                        counter in data.items() if time > 0})
        data = not_data
    return sum(data.values())
    #####    inefficient way    #####
    #day = 0                        #
    #while day < days:              #
    #    for t in range(len(data)): #
    #        if data[t] == 0:       #
    #            data[t] = 6        #
    #            data.append(8)     #
    #        else:                  #
    #            data[t] -= 1       #
    #    day += 1                   #
    #return len(data)               #
    #################################


def part1(data):
    """Solve part 1"""
    return main(data, 80)


def part2(data):
    """Solve part 2"""
    return main(data, 256)


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
