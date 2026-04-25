n, m = map(int, input().split())

floor = [list(input()) for _ in range(n)]
c = 0

for i in range(n):
  isCon = False
  for j in range(m):
    if floor[i][j] == "-":
      if not isCon:
        isCon = True
        c += 1
    else: isCon = False

for j in range(m):
  isCon = False
  for i in range(n):
    if floor[i][j] == "|":
      if not isCon:
        isCon = True
        c += 1
    else: isCon = False

print(c)
