n = int(input())
s = []
for _ in range(n):
  name, score, risk, cost = input().split()
  j = (int(score)**3) // (int(cost)*(int(risk)+1))
  s.append((j, cost, name))
s.sort(key=lambda x: (-x[0], x[1], x[2]))
print(s[1][2])
