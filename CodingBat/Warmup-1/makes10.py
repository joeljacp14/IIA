def makes10(a, b):
  sum = a + b
  if a == 10 or b == 10 or sum == 10:
    return True
  return False


print(makes10(9, 10))# → True
print(makes10(9, 9))# → False
print(makes10(1, 9))# → True