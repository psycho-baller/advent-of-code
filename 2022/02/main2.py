from pathlib import Path

inp = Path('input.txt').read_text().splitlines()
ans = 0



for game in inp:
    bot, me = game.split()
    if (me == "X"):
        if bot == "A":
            ans+=3
        elif bot == "B":
            ans+=1
        elif bot == "C":
            ans+=2
    elif (me == "Y"):
        ans+=3
        if bot == "B":
            ans+=2
        elif bot == "A":
            ans+=1
        elif bot == "C":
            ans+=3
    elif (me == "Z"):
        ans+=6
        if bot == "A":
            ans+=2
        elif bot == "B":
            ans+=3
        elif bot == "C":
            ans+=1
print(ans)

