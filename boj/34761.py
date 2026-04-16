n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = set(a)
ans = 1

for i in range(n):
  if a[i] != b[i]:
    ans = 0
    break

for i in range(n, n*2):
  if b[i] not in s:
    ans = 0
    break

print("YES" if ans else "NO")
