n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
j = 0
for i in range(len(a)):
    while j < m and b[j] != a[i]:
        j += 1
    j += 1
if j > m:
    print("No")
else:
    print("Yes")
