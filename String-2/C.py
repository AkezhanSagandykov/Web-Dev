def count_hi(str):
  counter = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      counter += 1
  return counter
