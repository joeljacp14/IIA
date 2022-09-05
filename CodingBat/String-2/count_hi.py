def count_hi(str):
  cont = 0
  for i in range(len(str) - 1):
    if str[i:i + 2] == "hi":
      cont += 1
  return cont


print(count_hi('abc hi ho'))# → 1
print(count_hi('ABChi hi'))# → 2
print(count_hi('hihi'))# → 2