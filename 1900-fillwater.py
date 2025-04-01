t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    for i in range(n): 
        if i+1<n and i+2<n and s[i:i+3] == "...":
            count = 2
            break
        elif s[i] == '.':
            count += 1
        else:
            pass
    print(count)