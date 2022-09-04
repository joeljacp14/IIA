def front3(str):
  if len(str) >= 3:
    front = str[:3]
    return front + front + front
  return str + str + str


print(front3('Python'))
print(front3('Chocolate'))# → 'ChoChoCho'
print(front3('abc'))# → 'abcabcabc'