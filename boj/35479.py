r, g, b = map(int, input().split())
rp, gp, bp = map(lambda x: x/255, (r, g, b))

k = 1-max((rp, gp, bp))
if k == 1: print(0, 0, 0, 1)
else:
  c = (1-rp-k)/(1-k)
  m = (1-gp-k)/(1-k)
  y = (1-bp-k)/(1-k)
  print(c, m, y, k)
