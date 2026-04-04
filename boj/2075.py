from sys import stdin

n = int(stdin.readline().rstrip())

q = [1000000002]

def insert(x):
  q.append(x)
  idx = len(q)-1

  while 1:
    if q[idx] <= q[idx//2]: break
    q[idx], q[idx//2] = q[idx//2], q[idx]
    idx = idx//2

  # print(*q)
  return

for _ in range(n):
  for i in map(int, stdin.readline().rstrip().split()):
    if len(q) == 1 or i >= q[-1]: insert(i)

# print(*q)

def remove():
  idx = 1
  q[idx], q[-1] = q[-1], q[idx]
  q.pop()

  while 1:
    check = idx*2 if idx*2 >= len(q) or idx*2+1 >= len(q) or q[idx*2] > q[idx*2+1] else idx*2+1

    if check >= len(q) or q[idx] >= q[check]: break
    q[idx], q[check] = q[check], q[idx]
    idx = check

  # print(*q)
  return

for _ in range(n-1): remove()

print(q[1])
