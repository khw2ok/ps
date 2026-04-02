n, m = map(int, input().split())

castle = [[0]*n for _ in range(m)]
mv = ["L", "U", "R", "D"]

cy, cx = m-1, 0
castle[cy][cx] = 1
direction = 0
cnt = 1

while cnt != n*m:
  if mv[direction%4] == "L":
    if cx+1 < n and not castle[cy][cx+1]:
      cx += 1
      castle[cy][cx] = 1
      cnt += 1
    else:
      direction += 1
      cy -= 1
      castle[cy][cx] = 1
      cnt += 1
  elif mv[direction%4] == "U":
    if cy-1 >= 0 and not castle[cy-1][cx]:
      cy -= 1
      castle[cy][cx] = 1
      cnt += 1
    else:
      direction += 1
      cx -= 1
      castle[cy][cx] = 1
      cnt += 1
  elif mv[direction%4] == "R":
    if cx-1 >= 0 and not castle[cy][cx-1]:
      cx -= 1
      castle[cy][cx] = 1
      cnt += 1
    else:
      direction += 1
      cy += 1
      castle[cy][cx] = 1
      cnt += 1
  elif mv[direction%4] == "D":
    if cy+1 < m and not castle[cy+1][cx]:
      cy += 1
      castle[cy][cx] = 1
      cnt += 1
    else:
      direction += 1
      cx += 1
      castle[cy][cx] = 1
      cnt += 1
  # print("\n".join([" ".join(map(str, i)) for i in castle]))
print(cx, m-cy-1)
