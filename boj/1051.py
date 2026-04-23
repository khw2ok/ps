n, m = map(int, input().split())

rec = [list(map(int, list(input()))) for _ in range(n)]
ans = 1

# print("\n".join(" ".join(map(str, i)) for i in rec))
# print()

for i in range(n-1):
  for j in range(m-1):
    # print(i, j, rec[i][j], n-i, m-j)
    for k in range(1, min(n-i, m-j)):
      if rec[i][j] == rec[i+k][j] == rec[i][j+k] == rec[i+k][j+k]:
        if (t := (k+1)**2) > ans: ans = t

print(ans)
