N = int(input())
n = N
temp = []
sum = 0
while len(temp) != n:
    N = int(input())
    temp.append(N)
for i in temp:
    sum += i
print(sum)