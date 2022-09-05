def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n >= 13 and n < 15 or n > 16 and n <= 19:
    return 0
  return n


print(no_teen_sum(1, 2, 3))# → 6
print(no_teen_sum(2, 13, 1))#→ 3
print(no_teen_sum(2, 1, 14))# → 3