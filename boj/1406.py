from sys import stdin

n = stdin.readline().rstrip()
m = int(stdin.readline().rstrip())

left = list(n)
right = []

for _ in range(m):
  cmd, *arg = stdin.readline().rstrip().split()

  if cmd == "L" and left: right.append(left.pop())
  elif cmd == "D" and right: left.append(right.pop())

  elif cmd == "B" and left: left.pop()

  elif cmd == "P": left.append(arg[0])

print("".join(left + right[::-1]))
