def date_fashion(you, date):
  if you >= 3 and you <= 10 and date >= 8:
    return 2
  elif you >= 8 and date >= 3 and date <= 10:
    return 2
  elif you >= 3 and you <= 10 and date <= 2:
    return 0
  elif you <= 2 and date >= 3 and date <= 10:
    return 0
  elif you <= 2 and date <= 2:
    return 0
  else:
    return 1
