def common_end(a, b):
  index = len(a) - 1
  index2 = len(b) - 1
  if a[index] == b[index2] or a[0] == b[0]:
    return True
  else:
    return False
a = [1, 2, 3]
b = [7, 3]
