t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = set(list(map(int, input().split())))
    if k in a:
        print("YES")
    else:
        print("NO")