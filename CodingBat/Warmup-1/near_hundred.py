def near_hundred(n):
  near100 = abs(100 - n)
  near200 = abs(200 - n)
  
  if near100 <= 10 or near200 <= 10:
    return True
  return False


print(near_hundred(93))# → True
print(near_hundred(90))# → True
print(near_hundred(89))# → False