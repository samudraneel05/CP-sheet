t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    x = input()
    s = input()
    count = 0
    while len(x) < m:
        x += x
        count += 1
    if s in x:
        print(count)
    elif s in x + x:
        print(count + 1)
    else:
        print(-1)