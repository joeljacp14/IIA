def make_bricks(small, big, goal):
  if goal > (big * 5 + small):
    return False
  if (goal % 5) > small:
    return False
  return True


print(make_bricks(3, 1, 8))# → True
print(make_bricks(3, 1, 9))#→ False
print(make_bricks(3, 2, 10))# → True