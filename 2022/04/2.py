from pathlib import Path

inp = Path('input.txt').read_text().splitlines()
# inp = Path('sample.txt').read_text().splitlines()

count = 0
for pair in inp:
    # logic
    # a-b,c-d
    # elf1 overlaps if a >= c and a <= d or b >= c and b <= d
    # elf2 overlaps if c >= a and c <= b or d >= a and d <= b
    
    
    # we will parse the line
    elf1, elf2 = pair.split(',')
    a, b = elf1.split('-')
    c, d = elf2.split('-')
    
    # convert to int
    a, b, c, d = int(a), int(b), int(c), int(d)
    
    # logic time
    if (( a >= c and a <= d) or (b >= c and b <= d)) or ((c >= a and c <= b) or (d >= a and d <= b)):
        count += 1
print(count)
