N = int(input())
K = 0
power = 1
while power < N:
    power *= 2
    K += 1
print(K)