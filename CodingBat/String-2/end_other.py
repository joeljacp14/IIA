def end_other(a, b):
  a = a.lower()
  b = b.lower()
  lena = len(a)
  lenb = len(b)
  if lena > lenb:
    if a.endswith(b):
      return True
  if b.endswith(a):
    return True
  return False


print(end_other('Hiabc', 'abc'))# → True
print(end_other('AbC', 'HiaBc'))# → True
print(end_other('abc', 'abXabc'))# → True