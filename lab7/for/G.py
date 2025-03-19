x = int(input())
temp = 0
for i in range(2, x + 1):
    if (x % i == 0):
        temp = i
        break
print(temp)