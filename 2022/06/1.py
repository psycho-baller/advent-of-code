from pathlib import Path

inp = Path('input.txt').read_text()
# inp = Path('sample.txt').read_text()

for i in range(4,len(inp)):
    sett = set(inp[i-4:i])
    
    if (len(sett) == 4):
        print(i)
        break
