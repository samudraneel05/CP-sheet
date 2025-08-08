def construct_tree():
    n = int(input())
    edges = []
    max_node = 0

    for i in range(n):
        u, v = map(int, input().split())
        weight = abs(v - u)
        edges.append((weight, u, v, i+1))
        max_node = max(max_node, u, v)

    edges.sort(key=lambda e: e[0], reverse=True)

    parent = list(range(max_node + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[rv] = ru
        return True

    selected = []

    for weight, u, v, idx in edges:
        if union(u, v):
            selected.append(idx)

    print(len(selected))
    print(' '.join(map(str, selected)))

t = int(input())
for _ in range(t):
    construct_tree()