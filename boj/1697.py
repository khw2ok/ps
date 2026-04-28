from collections import deque

n, k = map(int, input().split())
q = deque([n])
l = set([n])
t = 0

while k not in l:
  #if n == k: break
  for _ in range(len(q)):
    now = q.popleft()

    # if not (0 <= now <= 100000): q.popleft(); continue
    if (now-1 not in l) and (now-1 >= 0): q.append(now-1); l.add(now-1)
    if (now+1 not in l) and (now+1 <= 100_000): q.append(now+1); l.add(now+1)
    if (now*2 not in l) and (now*2 <= 100_000): q.append(now*2); l.add(now*2)

  t += 1

print(t)
