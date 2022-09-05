def first_half(str):
  return str[:int(len(str) / 2)]


print(first_half('WooHoo'))# → 'Woo'
print(first_half('HelloThere'))# → 'Hello'
print(first_half('abcdef'))# → 'abc'