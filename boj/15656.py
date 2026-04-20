n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

def bt(l: list):
  if len(l) == m:
    print(*l)
    return
  for i in a:
    bt(l+[i])
  return

bt([])
