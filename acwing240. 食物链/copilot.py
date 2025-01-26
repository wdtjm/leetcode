n, k = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
dist = [0] * (n + 1)

num = 0


def find(x):
    if parent[x] != x:
        root = find(parent[x])
        dist[x] += dist[parent[x]]
        parent[x] = root
    return parent[x]


def union(x, y, relation):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY
        dist[rootX] = dist[y] - dist[x] + relation
    else:
        if (dist[x] - dist[y]) % 3 != relation:
            return False
    return True


for i in range(k):
    o, x, y = map(int, input().split())
    if x > n or y > n or (o == 2 and x == y):
        num += 1
        continue

    if o == 1:
        if not union(x, y, 0):
            num += 1
    elif o == 2:
        if not union(x, y, 1):
            num += 1

print(num)