from pathlib import Path
import string

inp = Path('input.txt').read_text().splitlines()
ans=0
for i in range(0, len(inp), 3):
    first, second, third = inp[i], inp[i+1], inp[i+2]
    # print(len(first), len(second))
    for char in list(string.ascii_letters):
        if char in first and char in second and char in third:
            if char.islower():
                ans+= (ord(char) - ord("a") + 1)
            else:
                ans+= (ord(char) - ord("A") + 27)
print(ans)