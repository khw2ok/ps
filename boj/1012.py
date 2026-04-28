from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def Worm(fX, fY):
    if field[fY][fX] != 1: return
    field[fY][fX] = c
    if fX-1 >= 0: Worm(fX-1, fY)
    if fY+1 <= n-1: Worm(fX, fY+1)
    if fX+1 <= m-1: Worm(fX+1, fY)
    if fY-1 >= 0: Worm(fX, fY-1)
t = int(stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, stdin.readline().rstrip().split())
    field = [[0]*m for _ in range(n)]
    c = 2
    pLog = set()
    for _ in range(k):
        x, y = map(int, stdin.readline().rstrip().split())
        pLog.add((x, y))
        field[y][x] = 1
    for i in pLog:
        if field[i[1]][i[0]] != 1: continue
        Worm(i[0], i[1])
        c += 1
    print(c-2)
