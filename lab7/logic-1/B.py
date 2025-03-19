def caught_speeding(speed, is_birthday):
  if (is_birthday == False) and speed <= 60:
    return 0
  elif (is_birthday == False) and speed >= 61 and speed <= 80:
    return 1
  elif (is_birthday == False) and speed >= 81:
    return 2
  elif (is_birthday == True) and speed <= 65:
    return 0
  elif (is_birthday == True) and speed >= 66 and speed <= 85:
    return 1
  elif (is_birthday == True) and speed >= 86:
    return 2
is_birthday = True
