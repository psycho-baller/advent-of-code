"""AoC 3, 2021"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [str(i) for i in puzzle_input.splitlines()]


def binary_to_decimal(n):

    return int(n, 2)


def part1(data):
    """Solve part 1"""
    gamma = ''
    epsilon = ''
    for pos in range(len(data[0])):
        zero = one = 0
        for bin in data:
            if bin[pos] == '0':
                zero += 1
            elif bin[pos] == '1':
                one += 1
        if zero > one:

            gamma += '0'
            epsilon += '1'
        elif one > zero:
            gamma += '1'
            epsilon += '0'

    return binary_to_decimal(gamma) * binary_to_decimal(epsilon)


def part2(data):
    """Solve part 2"""
    def get(compound, data):
        numbers = data
        index = 0
        while len(numbers) > 1:
            zeroes = []
            ones = []
            zero = one = 0
            for bin in range(len(numbers)):
                if numbers[bin][index] == '0':
                    zero += 1
                    zeroes.append(numbers[bin])
                else:
                    one += 1
                    ones.append(numbers[bin])
            if compound == 'o2':
                if zero > one:
                    numbers = zeroes
                else:
                    numbers = ones
            else:
                if zero > one:
                    numbers = ones
                else:
                    numbers = zeroes
            index += 1
        binary = numbers[0]
        return binary_to_decimal(binary)
    return int(get('o2', data))*int(get('co2', data))


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
