N = int(input())  
lst = []  
for _ in range(N):
    command = input().split()  
    action = command[0]  
    args = command[1:]  

    if action == "insert":
        lst.insert(int(args[0]), int(args[1]))  
    elif action == "print":
        print(lst)  
    elif action == "remove":
        lst.remove(int(args[0]))  
    elif action == "append":
        lst.append(int(args[0]))  
    elif action == "sort":
        lst.sort()  
    elif action == "pop":
        lst.pop()  
    elif action == "reverse":
        lst.reverse()  