def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)  
string = input().strip()
i, c = input().split()
position = int(i)  
print(mutate_string(string, position, c))