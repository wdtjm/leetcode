n, m = map(int,input().split())
arr = list(map(int,input().split()))
i = 0
s = []
for k in range(len(arr)):
    if k == 0:
        s.append(arr[k])
    else:
        s.append(s[k-1]+arr[k])
while i < m:
    i += 1
    l, r = map(int,input().split())
    if l == 1:
        print(s[r-1])
    else:
        print(s[r-1]-s[l-2])

