n, k = map(int, input().split())
d = map(lambda x: n-int(x), input().split())

for i in d: print(n if i < n//2 else 1, end=" ")
