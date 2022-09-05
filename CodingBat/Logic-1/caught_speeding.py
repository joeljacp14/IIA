def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    if speed >= 61 and speed <= 80:
      return 1
  else:
    if speed <= (60 + 5):
      return 0
    if speed >= (61 + 5) and speed <= (80 + 5):
      return 1
  return 2


print(caught_speeding(60, False))# → 0
print(caught_speeding(65, False))# → 1
print(caught_speeding(65, True))# → 0