t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
        
    suma = sum(a)
    x = a.count(0)
    y = a.count(1)
    z = n - x - y

    m = s - suma
    if m < 0 or m == 1:
        output = []
        output.extend(['0'] * x)
        output.extend(['2'] * z)
        output.extend(['1'] * y)
        print(' '.join(output))
    else:
        print("-1")
