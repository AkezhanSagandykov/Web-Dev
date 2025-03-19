N = int(input())
numbers = list(map(int, input().split()))
i = 1
counter = 0
for i in range(1, N):
    if(numbers[i] > 0 and numbers[i - 1] > 0) or (numbers[i] < 0 and numbers[i - 1] < 0):
        counter += 1
if counter >= 1:
    print("YES")
else:
    print("NO")