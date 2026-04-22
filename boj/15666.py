n, m = map(int, input().split())
a = list(map(int, input().split()))
s = set()

a.sort()

def bt(l: list):
  if len(l) == m:
    if tuple(l) not in s:
      s.add(tuple(l))
      print(*l)
    return
  for i in a:
    if len(l) == 0 or l[-1] <= i: bt(l+[i])
  return

bt([])
