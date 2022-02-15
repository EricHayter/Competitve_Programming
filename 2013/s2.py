import sys

w = int(input())
m = int(input())
c = [int(input()) for c in range(0,m)]

for x in range(0,m-3):
    t = 0
    for i in range(0,4):
        t += c[x+i]
        if t > w:
            print(x+i)
            sys.exit()

