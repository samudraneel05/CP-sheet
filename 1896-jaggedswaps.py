t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if l[0] == 1:
        print('YES')
    else:
        print('NO')