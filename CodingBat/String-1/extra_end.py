def extra_end(str):
  last = str[len(str) - 2:]
  
  return last+last+last


print(extra_end('Hello'))# → 'lololo'
print(extra_end('ab'))# → 'ababab'
print(extra_end('Hi'))# → 'HiHiHi'