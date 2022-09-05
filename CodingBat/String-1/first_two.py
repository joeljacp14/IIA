def first_two(str):
  if len(str) >= 2:
    return str[0:2]
  return str


print(first_two('Hello'))# → 'He'
print(first_two('abcdefg'))# → 'ab'
print(first_two('ab'))# → 'ab'