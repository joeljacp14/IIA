def string_bits(str):
  nstr = ""
  for i in range(len(str)):
    if i % 2 == 0:
      nstr += str[i]
  return nstr


print(string_bits('Hello'))# → 'Hlo'
print(string_bits('Hi'))# → 'H'
print(string_bits('Heeololeo'))# → 'Hello'