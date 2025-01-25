n, m, q = map(int, input().split())
arr = []
s = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n+1):
    for j in range(m+1):
        if i != 0 and j != 0:
            s[i][j] = s[i][j-1] + s[i-1][j] + arr[i-1][j-1] - s[i-1][j-1]
for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1])

