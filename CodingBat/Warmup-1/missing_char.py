def missing_char(str, n):
  return str[:n] + str[n + 1:]


print(missing_char('kitten', 1))# → 'ktten'
print(missing_char('kitten', 0))# → 'itten'
print(missing_char('kitten', 4))# → 'kittn'