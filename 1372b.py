def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        if n % 2 == 0:
            print(n // 2, n // 2)
        else:
            p = n
            i = 3
            while i * i <= n:
                if n % i == 0:
                    p = i
                    break
                i += 2
            a = n // p
            b = n - a
            print(a, b)

solve()