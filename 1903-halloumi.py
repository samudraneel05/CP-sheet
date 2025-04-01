t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if k==1 and not all(l[i] <= l[i + 1] for i in range(n - 1)):
        print('no')
    else:
        print('yes')