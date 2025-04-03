t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())
    moves = [
        ( a,  b), ( a, -b), (-a,  b), (-a, -b),
        ( b,  a), ( b, -a), (-b,  a), (-b, -a)
    ]
    
    attackking = {(xk - dx, yk - dy) for dx, dy in moves}
    attackqueen = {(xq - dx, yq - dy) for dx, dy in moves}
    
    print(len(attackking & attackqueen))