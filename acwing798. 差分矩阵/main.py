n, m, q = map(int, input().split())
arr = []
d = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        # b[i][j] = a[i][j] - a[i][j-1] - a[i-1][j] + a[i-1][j-1]
        d[i][j] += arr[i][j]
        if i != 0:
            d[i][j] -= arr[i-1][j]
        if j != 0:
            d[i][j] -= arr[i][j-1]
        if i != 0 and j != 0:
            d[i][j] += arr[i-1][j-1]
for i in range(q):
    y1, x1, y2, x2, c = map(int, input().split())
    # d[y1][x1] += c
    # d[y2+1][x1] -= c
    # d[y1][x2+1] -= c
    # d[y2+1][x2+1] += c
    # x, y映射到列表下标，对应值要减1
    d[y1-1][x1-1] += c
    if y2 < n:
        d[y2][x1-1] -= c
    if x2 < m:
        d[y1 - 1][x2] -= c
    if y2 < n and x2 < m:
        d[y2][x2] += c

re = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        # re[i][j] = d[i][j] + re[i-1][j] + re[i][j-1] - re[i-1][j-1]
        re[i][j] += d[i][j]
        if i != 0:
            re[i][j] += re[i - 1][j]
        if j != 0:
            re[i][j] += re[i][j - 1]
        if i != 0 and j != 0:
            re[i][j] -= re[i - 1][j - 1]
for i in range(n):
    print(' '.join(list(map(str,re[i]))))





