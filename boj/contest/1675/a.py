n = int(input())

for i in range(n): print(f"{' '*(2*n-1-i)}*{' '*n}*{' '*(2*i+1)}*{' '*(n-1-i)}")

for i in range(n): print(f"{' '*(n-1-i)}*{' '*(n+1+2*(i))}*{' '*(2*(n-i)-1)}*{' '*i}")
