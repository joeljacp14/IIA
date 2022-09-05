def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(n):
  if (n % 10) >= 5:
    return int(((n + 10) / 10) * 10)
  return int((n / 10) * 10)


print(round_sum(16, 17, 18))# → 60
print(round_sum(12, 13, 14))# → 30
print(round_sum(6, 4, 4))# → 10