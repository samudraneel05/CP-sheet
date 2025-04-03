t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(max(a[0],2*(x-a[0])))
    else:
        print(max(a[0], 2*(x-a[-1]), max((a[i+1] - a[i]) for i in range(n-1))))
