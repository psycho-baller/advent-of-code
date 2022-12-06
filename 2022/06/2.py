from pathlib import Path

inp = Path('input.txt').read_text()
# inp = Path('sample.txt').read_text()
distinct_nums = 14
for i in range(distinct_nums,len(inp)):
    sett = set(inp[i-distinct_nums:i])
    
    if (len(sett) == distinct_nums):
        print(i)
        break
