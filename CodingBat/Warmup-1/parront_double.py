def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
  return False


print(parrot_trouble(True, 6)) #→ True
print(parrot_trouble(True, 7)) #→ False
print(parrot_trouble(False, 6)) #→ False