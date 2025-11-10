MOD = 10**9 + 7

def getCount(arr):
    if not arr:
        return 1
    vals = sorted(set(arr))
    prev = 0
    ans = 1
    for v in vals:
        ans = (ans * (v - prev + 1)) % MOD
        prev = v
    return ans

input_arr = [0, 1, 2, 3]
print(getCount(input_arr))