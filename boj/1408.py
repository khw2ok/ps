h, m, s = map(int, input().split(":"))
cur = h*3600+m*60+s

h, m, s = map(int, input().split(":"))
start = h*3600+m*60+s

res = start-cur
if res < 0: res = 24*3600-cur+start

ans = []

for _ in range(3):
  ans.append(res % 60)
  res //= 60

print(":".join(f"{i:02}" for i in ans[::-1]))
