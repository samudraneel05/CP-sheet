t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    result = 0
    for num in s:
        if num != 0:
            result += num
        if num == 0:
            result += 1
    
    print(result)