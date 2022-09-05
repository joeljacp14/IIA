def alarm_clock(day, vacation):
  if not vacation:
    if day >= 1 and day <= 5:
      return "7:00"
    return "10:00"
  else:
    if day >= 1 and day <= 5:
      return "10:00"
    return "off"


print(alarm_clock(1, False))# → '7:00'
print(alarm_clock(5, False))# → '7:00'
print(alarm_clock(0, False))# → '10:00'