
def min_price_sol(N, x, a):
    # sum_for_k[k] will store sum of minimal buy-costs for all types if we allow up to k rotations
    sum_for_k = [0] * N

    # For each target type index i (0-based), accumulate min costs for k = 0..N-1
    # mn will be min cost among positions that carry this type after 0..k rotations
    for i in range(N):
        mn = 10**30
        for k in range(N):
            # position that has this type after k rotations is (i - k) mod N (0-based)
            idx = (i - k) % N
            if a[idx] < mn:
                mn = a[idx]
            sum_for_k[k] += mn

    ans = 10**30
    for k in range(N):
        cost = sum_for_k[k] + k * x
        if cost < ans:
            ans = cost
    return ans

print(min_price_sol(3, 5, [1, 10, 1]))