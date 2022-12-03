"""AoC 9, 2021"""

# Standard library imports
import pathlib
import sys
import collections
from numpy import prod


def parse(puzzle_input):
    """Parse input"""
    # return [list(map(int, number)) for number in [list(line) for line in puzzle_input.splitlines()]]

    coords = collections.defaultdict(lambda: 9)

    for r, line in enumerate(puzzle_input.splitlines()):
        for c, num in enumerate(line):
            coords[(r, c)] = int(num)
    return coords


def adg(x: int, y: int):
    yield x+1, y
    yield x-1, y
    yield x, y-1
    yield x, y+1


def part1(data):
    """Solve part 1"""
    # list for part 2
    global holes
    holes = []

    answer = 0
    for (x, y), n in data.items():
        if all(data.get((x, y), 9) > n for (x, y) in adg(x, y)):
            holes.append((x, y))
            answer += n+1
    return answer


''' NOOB ANSWER:
    shorties = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if r == 0:
                if data[r][c] < data[r+1][c]:
                    if c == len(data[0])-1 and data[r][c] < data[r][c-1]:
                        #left and bottom
                        shorties.append(data[r][c])
                    elif c == 0 and data[r][c] < data[r][c+1]:
                        #right and bottom
                        shorties.append(data[r][c])
                    elif data[r][c] < data[r][c+1] and data[r][c] < data[r][c-1]:
                        # right left bottom
                        shorties.append(data[r][c])

            elif r == len(data)-1:
                if data[r][c] < data[r-1][c]:
                    if c == len(data[0])-1 and data[r][c] < data[r][c-1]:
                        #left and up
                        shorties.append(data[r][c])
                    elif c == 0 and data[r][c] < data[r][c+1]:
                        #right and up
                        shorties.append(data[r][c])
                    elif data[r][c] < data[r][c+1] and data[r][c] < data[r][c-1]:
                        # right left up
                        shorties.append(data[r][c])

            elif c == 0:
                if data[r][c] < data[r][c+1]:
                    if r == len(data)-1 and data[r][c] < data[r+1][c]:
                        #right and down
                        shorties.append(data[r][c])
                    elif r == 0 and data[r][c] < data[r-1][c]:
                        #right and up
                        shorties.append(data[r][c])
                    else:
                        shorties.append(data[r][c])

            elif c == len(data[0])-1:
                if data[r][c] < data[r][c-1]:
                    if r == len(data)-1 and data[r][c] < data[r-1][c]:
                        #left and down
                        shorties.append(data[r][c])
                    elif r == 0 and data[r][c] < data[r+1][c]:
                        #left and up
                        shorties.append(data[r][c])
                    else:
                        shorties.append(data[r][c])

            else:
                if data[r][c] < data[r+1][c] and data[r][c] < data[r-1][c] and data[r][c] < data[r][c+1] and data[r][c] < data[r][c-1]:
                    shorties.append(data[r][c])
    return sum(x+1 for x in shorties)
'''


def part2(data, holes):
    """Solve part 2"""
    basins = []

    for (x, y) in holes:
        todo = [(x, y)]
        seen = set()

        while todo:
            x, y = todo.pop()
            seen.add((x, y))

            for coord in adg(x, y):
                if coord not in seen and data[coord] != 9:
                    todo.append(coord)
        basins.append(len(seen))
    basins.sort()
    return prod(basins[-3:])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data, holes)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
