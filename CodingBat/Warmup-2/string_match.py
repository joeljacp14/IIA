def string_match(a, b):
  strshort = min(len(a), len(b))
  cont = 0
  
  for i in range(strshort - 1):
    substra = a[i:i + 2]
    substrb = b[i:i + 2]
    if substra == substrb:
      cont += 1
  
  return cont


print(string_match('xxcaazz', 'xxbaaz'))# → 3
print(string_match('abc', 'abc'))# → 2
print(string_match('abc', 'axc'))# → 0