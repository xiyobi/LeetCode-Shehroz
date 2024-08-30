S = ["--X","X++","X++"]
# d = ["++X","++X","X++"]
# x = ["X++","++X","--X","X--"]
sm = 0
for i in S:
    if i == "++X" or  i=="X++":
        sm += 1
    elif i == "--X" or i == "X--":
        sm += -1
print(sm) 