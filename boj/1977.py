m = int(input())
n = int(input())
ans = []
for i in range(1, 101):
  if m <= (t := i**2) <= n: ans.append(t)

if ans:
  print(sum(ans))
  print(ans[0])
else: print(-1)
