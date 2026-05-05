from sys import stdin

n = int(stdin.readline().rstrip())

s = 0
l = []
f = {}
mx = -4000
mn = 4000

for _ in range(n):
  d = int(stdin.readline().rstrip())

  s += d
  l.append(d)

  if d not in f: f[d] = 0
  f[d] += 1

  if d > mx: mx = d
  if d < mn: mn = d

l.sort()
fl = list(f.items())
fl.sort(key=lambda x: (x[1], x[0]))
fl = list(filter(lambda x: x[1] == fl[-1][1], fl))

print(round(s/n+0.000001))
print(l[n//2])
print(fl[1][0] if len(fl) >= 2 else fl[0][0])
print(mx-mn)
