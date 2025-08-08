from collections import deque

def min_weird_shop_cost(A, B):
    n = len(A)
    best = float('inf')
    A2 = A + A  # length 2n

    for R in range(n):   # window size w=R+1
        w = R+1
        s = 0
        dq = deque()
        
        # Compute sliding window min for first n windows
        for i in range(len(A2)):
            # remove elements not useful (larger than current)
            while dq and A2[dq[-1]] >= A2[i]:
                dq.pop()
            dq.append(i)
            
            # remove elements out of the window
            if dq[0] <= i - w:
                dq.popleft()
            
            # starting from i>=w-1, we have a valid window
            if i >= w-1 and i - (w-1) < n:
                s += A2[dq[0]]
        
        cost = s + R * B
        best = min(best, cost)

    return best

# Test cases
print(min_weird_shop_cost([7, 4, 2, 1], B=3))   # → 11
print(min_weird_shop_cost([1, 10, 10], B=1))    # → 5
