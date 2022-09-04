def front_back(str):
  if len(str) > 1:
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0]
  return str


print(front_back('code'))# → 'eodc'
print(front_back('a'))# → 'a'
print(front_back('ab'))# → 'ba'