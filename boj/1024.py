n, l = map(int, input().split())
a = (2*n/l-l+1)/2
if a < 0: a = -0.1
while a != int(a):
  l += 1
  a = (2*n/l-l+1)/2
  if a < 0 or l > 100: print(-1); break
else:
  print(*[i for i in range(int(a), int(a)+l)])
