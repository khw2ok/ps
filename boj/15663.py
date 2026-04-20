n, m = map(int, input().split())
a = list(map(int, input().split()))
s = set()

a.sort()

d = {}
for i in a:
  if i not in d: d[i] = 0
  d[i] += 1

def bt(l: list, d: dict):
  if len(l) == m:
    if tuple(l) not in s:
      s.add(tuple(l))
      print(*l)
    return
  for i in a:
    if d[i] > 0:
      d[i] -= 1
      bt(l+[i], d)
      d[i] += 1
  return

bt([], d)
