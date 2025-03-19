N = int(input())
numbers = list(map(int, input().split()))
counter = 0
i = 1
for i in range(1, N - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        counter += 1
print(counter)