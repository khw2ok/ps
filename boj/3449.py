t = int(input())
for _ in range(t):
  a = input()
  b = input()
  c = 0

  for i in zip(a, b):
    if i[0] != i[1]: c += 1

  print(f"Hamming distance is {c}.")
