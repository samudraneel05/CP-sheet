import math
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    diff = [abs(p[i]-i-1) for i in range(n)]
    print(math.gcd(*diff))