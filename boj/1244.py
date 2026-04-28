n = int(input())
sw = list(map(int, input().split()))

toggle = lambda x: 0 if x else 1

m = int(input())
for _ in range(m):
  gen, num = map(int, input().split())

  if gen == 1:
    for i in range(1, n+1):
      if i%num == 0: sw[i-1] = toggle(sw[i-1])

  else:
    num -= 1

    sw[num] = toggle(sw[num])
    for i in range(1, n):
      if num-i < 0 or num+i >= n: break
      if sw[num-i] != sw[num+i]: break
      sw[num-i] = toggle(sw[num-i])
      sw[num+i] = toggle(sw[num+i])

for i in range(n):
  print(sw[i], end=" ")
  if (i+1)%20 == 0: print()
