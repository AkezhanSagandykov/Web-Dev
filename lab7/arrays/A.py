N = int(input())
numbers = list(map(int, input().split()))
index = 0
for i in numbers:
    if index % 2 == 0:
        print(i, end=" ")
    index += 1