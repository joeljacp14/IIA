def last2(str):
  if len(str) < 2:
    return 0
  else:
    last = str[len(str) - 2:]
    cont = 0
    for i in range(len(str) - 2):
      substr = str[i:i + 2]
      if substr == last:
        cont += 1
    return cont


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))# → 1
print(last2('axxxaaxx'))# → 2