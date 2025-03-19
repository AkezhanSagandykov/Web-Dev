N = int(input())
n = N
temp = []
counter = 0
while len(temp) != n:
    N = int(input())
    temp.append(N)
for i in temp:
    if i == 0:
        counter += 1
print(counter)