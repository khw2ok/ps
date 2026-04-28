from sys import stdin
n, m = map(int, stdin.readline().rstrip().split())

b = []
bad1 = []
bad2 = []
bps1 = [[0 for _ in range(m+1)]]
bps2 = [[0 for _ in range(m+1)]]

for i in range(n):
  b.append([])

  for j in list(input()):
    if j == "W": b[-1].append(0)
    else: b[-1].append(1)

for i in range(n):
  bad1.append([])
  bad2.append([])
  for j in range(m):
    bad1[i].append(1 if b[i][j] == (i+j)%2 else 0)
    bad2[i].append(1 if b[i][j] != (i+j)%2 else 0)

for i in range(n):
  bps1.append([0])
  bps2.append([0])
  for j in range(m):
    bps1[i+1].append(bps1[i][j+1] + bps1[i+1][j] - bps1[i][j] + bad1[i][j])
    bps2[i+1].append(bps2[i][j+1] + bps2[i+1][j] - bps2[i][j] + bad2[i][j])

# print()
# print(bps1)
# print(bps2)
ans = []

for i in range(1, n-8+2):
  for j in range(1, m-8+2):
    ans.append(bps1[i+7][j+7] - bps1[i+7][j-1] - bps1[i-1][j+7] + bps1[i-1][j-1])
    ans.append(bps2[i+7][j+7] - bps2[i+7][j-1] - bps2[i-1][j+7] + bps2[i-1][j-1])
    # print(i, j, bps1[i+7][j+7] - bps1[i+7][j-1] - bps1[i-1][j+7] + bps1[i-1][j-1], bps2[i+7][j+7] - bps2[i+7][j-1] - bps2[i-1][j+7] + bps2[i-1][j-1])

print(min(ans))
