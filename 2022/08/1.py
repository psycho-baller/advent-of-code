from pathlib import Path

# inp = Path('input.txt').read_text().splitlines()
inp = Path('sample.txt').read_text().splitlines()

ans = 0

# turn into a 2d list
inp = [list(string) for string in inp]

# parseInt
# inp = [ int(v) for v in [array for array in inp]]
inp2 = []
for array in inp:
    line = []
    for v in array:
        line.append(int(v))
    inp2.append(line)
       
for r, line in enumerate(inp2):

    for c, val in enumerate(line):
        vis_up = True
        vis_down = True
        vis_left = True
        vis_right = True
        # an unwritten rule in my ..
        # if r == 0 or r == len(inp2)-1 or c == 0 or c == len(line)-1:
        #     # ans+=1
        #     pass
        # else:
        # check up
        row = r
        while row >= 1:
            row-=1
            # v = 
            if inp2[row][c] > val:
                vis_up = False
        # check down
        row = r
        while row < len(inp2)-1:
            row+=1
            if inp2[row][c] > val:
                vis_down = False
        # check left
        col = c
        while col >= 1:
            col-=1
            if line[col] > val:
                vis_left = False
        # check right
        col = c
        while col < len(line)-1:
            col+=1
            if line[col] > val:
                vis_right = False
        if vis_down or vis_left or vis_right or vis_up:
            ans+=1
            

print(ans)