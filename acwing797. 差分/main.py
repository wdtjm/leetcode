n, m = map(int, input().split())
arr = list(map(int, input().split()))
b = [arr[i+1] - arr[i] for i in range(n-1)]
b.insert(0, arr[0])
for i in range(m):
    l, r, c = map(int, input().split())
    b[l-1] += c
    if r != n:
        b[r] -= c
a = [b[0]]
for i in range(1,n):
    a.append(a[i-1] + b[i])
print(' '.join(list(map(str,a))))
