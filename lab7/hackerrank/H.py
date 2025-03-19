n = int(input())
arr = map(int, input().split())
arr = list(arr)
max = -1000
max2 = max
for i in arr:
    if i > max:
        max = i
for i in arr:
    if i != max:
        if i > max2:
            max2 = i
print(max2)