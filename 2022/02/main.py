from pathlib import Path

inp = Path('input.txt').read_text().splitlines()
ans = 0



for game in inp:
    bot, me = game.split()
    if (me == "X"):
        ans+=1
        if bot == "A":
            ans+=3
        elif bot == "C":
            ans+=6
    elif (me == "Y"):
        ans+=2
        if bot == "B":
            ans+=3
        elif bot == "A":
            ans+=6
    elif (me == "Z"):
        ans+=3
        if bot == "C":
            ans+=3
        elif bot == "B":
            ans+=6
print(ans)

