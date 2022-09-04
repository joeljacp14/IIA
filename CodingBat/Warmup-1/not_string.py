def not_string(str):
  if len(str) >= 3:
    if str[:3] == "not":
      return str
  return "not "+str


print(not_string('candy'))# → 'not candy'
print(not_string('x'))# → 'not x'
print(not_string('not bad'))# → 'not bad'