from pathlib import Path

txt =[ sum([int(j) for j in i.split("\n")]) for i in Path('input.txt').read_text().split("\n\n")]
txt.sort(reverse=True)

print(sum(txt[:3]))
