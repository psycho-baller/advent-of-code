from pathlib import Path

# inp = Path('input.txt').read_text().splitlines()
stack_data, actions = Path('sample.txt').read_text().split("\n\n")
stack_data = stack_data.splitlines()
stacks = {}
numbers = stack_data.pop()

# parse stacks
for i in numbers:
    if i != " ":
        stacks[int(i)] = []
    
for line in reversed(stack_data):
    for i in range(1, len(line), 4):
        if line[i] != " ":
            key = (i-1)//4 + 1
            stacks[key].append(line[i])

# 