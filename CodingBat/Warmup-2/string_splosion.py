def string_splosion(str):
  nstr = ""
  for i in range(len(str)):
    nstr += str[:i + 1]
  return nstr


print(string_splosion('Code'))# → 'CCoCodCode'
print(string_splosion('abc'))# → 'aababc'
print(string_splosion('ab'))#→ 'aab'
