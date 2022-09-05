def lone_sum(a, b, c):
  if a == b and b == c and a == c:
    return 0
  if a == b:
    return c
  if a == c:
    return b
  if b == c:
    return a
  return a + b + c


print(lone_sum(1, 2, 3))# → 6
print(lone_sum(3, 2, 3))#→ 2
print(lone_sum(3, 3, 3))# → 0