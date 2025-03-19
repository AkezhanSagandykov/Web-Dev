def near_ten(num):
  if 0 <= num % 10 <= 2:
    return True
  elif 8 <= num % 10 <= 9:
    return True
  else:
    return False