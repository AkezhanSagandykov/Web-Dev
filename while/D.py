N = int(input())
i = 0
power_of_two = 0
while 2**i <= N:
    power_of_two = 2**i
    i += 1
if N == power_of_two:
    print("YES")
else:
    print("NO")