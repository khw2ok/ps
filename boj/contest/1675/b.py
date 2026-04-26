from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
  n = int(stdin.readline().rstrip())
  a, b, c = 0, 0, 0
  d = 0
  can = True

  p = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

  for ai, bi, ci, pi in p:
    if ai > a:
      d += ai-a
      a += ai-a

    if bi > b:
      d += bi-b
      b += bi-b

    if ci > c:
      d += ci-c
      c += ci-c

    d += 1
    if d > pi: can = False

  print("YES" if can else "NO")
