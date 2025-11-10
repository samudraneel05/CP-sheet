from collections import Counter
from typing import List
def process_operations(pri, sec, operations):
    pcnt = Counter(pri)   
    scnt = Counter(sec)       
    res = []
    for op in operations:
        if not op:
            continue
        t = op[0]
        if t == 0:
            _, idx, newval = op
            oldval = sec[idx]  # assumes idx valid (0-based)
            if oldval != newval:
                scnt[oldval] -= 1
                if scnt[oldval] == 0:
                    del scnt[oldval]
                scnt[newval] += 1
                sec[idx] = newval
        elif t == 1:
            _, target = op
            total = 0
            for a, cnt_a in pcnt.items():
                total += cnt_a * scnt.get(target - a, 0)
            res.append(total)

    return res


print(process_operations([1, 2, 3], [3, 4],[[1,5],[0,0,1],[1,5]]))

print(process_operations([1, 2, 2], [2, 3],[[1,4],[0,0,3],[1,5]]))