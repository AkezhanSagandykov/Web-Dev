def alarm_clock(day, vacation):
  if 1 <= day <= 5 and vacation == False:
    return '7:00'
  elif (day == 6 or day == 0) and vacation == True:
    return 'off'
  elif 1 <= day <= 5 and vacation == True:
    return '10:00'
  else:
    return '10:00'
