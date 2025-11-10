import sys

MOD = 10**9 + 7

def output(x):
    sys.stdout.write(str(x) + "\n")

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    pow2 = [1] * 60
    for i in range(1, 60):
        pow2[i] = (pow2[i-1] * 2) % MOD

    for _ in range(t):
        n = int(input().strip())
        arr = []
        while len(arr) < n:
            arr.extend(map(int, input().split()))
        cnt = [0] * 60

        for v in arr:
            u = v
            while u:
                lb = u & -u
                idx = lb.bit_length() - 1
                cnt[idx] += 1
                u &= u - 1

        cntPow = [0] * 60
        deltaPow = [0] * 60
        TOT = 0
        for b in range(60):
            cntPow[b] = (cnt[b] * pow2[b]) % MOD
            TOT = (TOT + cntPow[b]) % MOD
        n_mod = n % MOD
        for b in range(60):
            deltaPow[b] = ((n_mod - cnt[b]) % MOD) * pow2[b] % MOD

        ans = 0
        for v in arr:
            Aj = 0
            Bj = TOT
            u = v
            while u:
                lb = u & -u
                idx = lb.bit_length() - 1
                Aj += cntPow[idx]
                if Aj >= MOD:
                    Aj -= MOD
                Bj += deltaPow[idx]
                if Bj >= MOD:
                    Bj -= MOD
                u &= u - 1
            ans = (ans + Aj * Bj) % MOD

        output(ans)

if __name__ == "__main__":
    main()