t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq_dict = {}
    for element in a:
        freq_dict[element] = freq_dict.get(element, 0) + 1
    
    if len(freq_dict)>=3:
        print("No")
    elif len(freq_dict)==1:
        print("Yes")
    else:
        x, y = freq_dict.values()
        if x == y or (n % 2 == 1 and abs(x - y) == 1):
            print("Yes")
        else:
            print("No")