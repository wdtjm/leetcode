n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
for i in range(len(a)):
    if a[i] + b[j] > x:
        while j > 0 and a[i] + b[j] > x:
            j -= 1
    if a[i] + b[j] < x:
        while j < m - 1 and a[i] + b[j] < x:
            j += 1
    if a[i] + b[j] == x:
        print(str(i) + ' ' + str(j))
        break


