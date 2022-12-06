from pathlib import Path

stack_data, actions = Path('input.txt').read_text().split("\n\n")
# stack_data, actions = Path('sample.txt').read_text().split("\n\n")
stack_data = stack_data.splitlines()
actions = actions.splitlines()
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

# do actions
for action in actions:
    # move 1 from 2 to 1
    nums= action.split()
    nums.remove("move")
    nums.remove("from")
    nums.remove("to")
    nums = [int(i) for i in nums]
    amount, frm, to = nums
    stacks[frm], taken = stacks[frm][:-amount], stacks[frm][-amount:]
    stacks[to] += taken
    # print(stacks[frm], stacks[to])
ans = ""
for i in range(1,len(stacks)+1):
    ans += stacks[i].pop()
print(ans)