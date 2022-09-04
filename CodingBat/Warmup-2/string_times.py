def string_times(str, n):
  nstr = ""
  for i in range(n):
    nstr += str
  return nstr


print(string_times('Hi', 2))# → 'HiHi'
print(string_times('Hi', 3))# → 'HiHiHi'
print(string_times('Hi', 1))# → 'Hi'