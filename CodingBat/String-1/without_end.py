def without_end(str):
  length = len(str)
  if length >= 2:
    return str[1: length - 1]
  return str


print(without_end('Hello'))# → 'ell'
print(without_end('java'))# → 'av'
print(without_end('coding'))# → 'odin'