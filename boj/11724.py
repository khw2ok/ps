from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())

g = [
  [1 if i == j else 0 for j in range(n)] for i in range(n)
]


for _ in range(m):
  u, v = map(lambda x: int(x)-1, stdin.readline().rstrip().split())

  g[u][v] = 1
  g[v][u] = 1

s = [0]*n
c = 0

q = deque()

for i in range(n): # 첫 번째 정점부터 탐색
  if s[i]: continue # 이미 탐색된 정점인 경우 스킵

  q.append(g[i])
  s[i] = 1
  c += 1

  while q:
    cur = q.popleft()

    for i in range(n):
      if cur[i]:
        if s[i]: continue # 이미 탐색된 정점인 경우 스킵
        q.append(g[i])
        s[i] = 1

# print()
# print("\n".join(", ".join(map(str, i )) for i in g))
print(c)
