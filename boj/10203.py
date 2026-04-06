for _ in range(int(input())):
  c = 0
  for i in (s:=input()):
    if i in ('a', 'e', 'i', 'o', 'u'): c += 1
  print(f"The number of vowels in {s} is {c}.")
