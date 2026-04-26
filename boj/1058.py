n = int(input())
g = [[1 if i == "Y" else 0 for i in input()] for _ in range(n)]

def search(x: int, vis: set, level: int) -> set:
  if level == 0: return vis

  t = set()|vis

  for i in range(n):
    if (g[x][i]) and (i not in vis):
      vis.add(i)
      t = t|search(i, vis, level-1)
      vis.remove(i)

  return t

mx = 0
for i in range(n):
  if mx < (t := len(search(i, set([i]), 2))-1): mx = t

print(mx)
