def squirrel_play(temp, is_summer):
  if is_summer:
    if temp >= 60 and temp <= 100:
      return True
  else:
    if temp >= 60 and temp <= 90:
      return True
  return False


print(squirrel_play(70, False))# → True
print(squirrel_play(95, False))# → False
print(squirrel_play(95, True))#→ True