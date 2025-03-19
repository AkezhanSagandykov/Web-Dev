N = int(input())
numbers = list(map(int, input().split()))
for i in numbers[::-1]:
    print(i, end=" ")