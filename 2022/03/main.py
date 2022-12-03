from pathlib import Path
import string

inp = Path('input.txt').read_text().splitlines()
ans=0
for line in inp:
    first, second = line[:len(line)//2], line[len(line)//2:]
    # print(len(first), len(second))
    for char in list(string.ascii_letters):
        if char in first and char in second:
            if char.islower():
                ans+= (ord(char) - ord("a") + 1)
            else:
                ans+= (ord(char) - ord("A") + 27)
print(ans)