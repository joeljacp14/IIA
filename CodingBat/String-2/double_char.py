def double_char(str):
  nstr = ""
  for i in str:
    nstr += i + i
  return nstr


print(double_char('The'))# → 'TThhee'
print(double_char('AAbb'))# → 'AAAAbbbb'
print(double_char('Hi-There'))#→ 'HHii--TThheerree'