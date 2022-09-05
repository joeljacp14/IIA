def left2(str):
  length = len(str)
  if(length > 2):
    return str[2:length]+str[:2]
  return str


print(left2('Hello'))# → 'lloHe'
print(left2('java'))# → 'vaja'
print(left2('Hi'))# → 'Hi'