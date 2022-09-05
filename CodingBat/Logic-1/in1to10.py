def in1to10(n, outside_mode):
  if not outside_mode:
    if n >= 1 and n <= 10:
      return True
  else:
    if n <= 1 or n >= 10:
      return True
  return False


print(in1to10(5, False))# → True
print(in1to10(11, False))# → False
print(in1to10(11, True))# → True