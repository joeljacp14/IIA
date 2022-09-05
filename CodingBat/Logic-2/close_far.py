def close_far(a, b, c):
  if is_close(a, b) and is_far(a, b, c) or is_close(a, c) and is_far(a, c, b):
    return True
  return False
  
def is_close(a, b):
  if abs(a - b) <= 1:
    return True
  return False
    
def is_far(a, b, c):
  if abs(a - c) >= 2 and abs(b - c) >= 2:
    return True
  return False


print(close_far(1, 2, 10))# → True
print(close_far(1, 2, 3))# → False
print(close_far(4, 1, 3))# → True