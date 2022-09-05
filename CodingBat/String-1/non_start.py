def non_start(a, b):
  return a[1:len(a)]+b[1:len(b)]


print(non_start('Hello', 'There'))# → 'ellohere'
print(non_start('java', 'code'))# → 'avaode'
print(non_start('shotl', 'java'))# → 'hotlava'