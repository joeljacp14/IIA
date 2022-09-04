def front_times(str, n):
  nstr = ""
  if len(str) >= 3:
    for i in range(n):
      nstr += str[:3]
    return nstr
  else:
    for i in range(n):
      nstr += str
    return nstr


print(front_times('Chocolate', 2))#→ 'ChoCho'
print(front_times('Chocolate', 3))# → 'ChoChoCho'
print(front_times('Abc', 3))# → 'AbcAbcAbc'