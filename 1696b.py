import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        l = 0
        while l < n and a[l] == 0:
            l += 1
        if l == n:
            print(0)
            continue
        r = n - 1
        while r >= 0 and a[r] == 0:
            r -= 1
        if 0 in a[l:r+1]:
            print(2)
        else:
            print(1)

if __name__ == "__main__":
    solve()