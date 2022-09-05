def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str) - 2):
    if str[i:i + 3] == "cat":
      cat += 1
    if str[i:i + 3] == "dog":
      dog += 1
  if cat == dog:
    return True
  return False


print(cat_dog('catdog'))# → True
print(cat_dog('catcat'))# → False
print(cat_dog('1cat1cadodog'))# → True