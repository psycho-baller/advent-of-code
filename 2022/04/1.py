from pathlib import Path

inp = Path('input.txt').read_text().splitlines()
# inp = Path('sample.txt').read_text().splitlines()

count = 0
for pair in inp:
    # logic
    # a-b,c-d
    # we need a >= c and b <= d
    # or a <= c and b >= d
    
    # we will parse the line
    elf1, elf2 = pair.split(',')
    a, b = elf1.split('-')
    c, d = elf2.split('-')
    
    # convert to int
    a, b, c, d = int(a), int(b), int(c), int(d)
    
    # logic time
    if (a >= c and b <= d) or (a <= c and b >= d):
        count += 1
print(count)