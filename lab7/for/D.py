x = int(input())
d = int(input())
numbers = str(x)
counter = 0
for i in numbers:
    if int(i) == d:
        counter += 1
print(counter)