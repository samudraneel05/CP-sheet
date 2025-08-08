class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def update(self, i, v):
        while i <= self.n:
            self.tree[i] += v
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

def buildfenwick():
    n = int(input())
    a = [0] + list(map(int, input().split()))

    L = [0] * (n + 1)
    R = [0] * (n + 1)

    bit = BIT(n)
    B = 0

    for k in range(1, n+1):
        L[k] = bit.query(n) - bit.query(a[k])
        B += L[k]
        bit.update(a[k], 1)

    bit = BIT(n)

    for k in range(n, 0, -1):
        R[k] = bit.query(n) - bit.query(a[k])
        bit.update(a[k], 1)

    m = B
    for k in range(1, n+1):
        c = R[k] - L[k]
        if c < 0:
            m += c

    print(m)


t = int(input())
for _ in range(t):
    buildfenwick()
