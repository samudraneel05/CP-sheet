t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    pointer = n*k
    while k!=0:
        pointer -= n//2+1
        ans += a[pointer]
        k -= 1
    print(ans)