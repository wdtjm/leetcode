def find_l(k, a):
    i = -1
    j = len(a)
    while i != j - 1:
        mid = (i + j) >> 1
        if a[mid][0] < k:
            i = mid
        else:
            j = mid
    return j


def find_r(k, a):
    i = -1
    j = len(a)
    while i != j - 1:
        mid = (i + j) >> 1
        if a[mid][0] <= k:
            i = mid
        else:
            j = mid
    return i


def getKey(item):
    return item[0]


n, m = map(int, input().split())

a = list()

for i in range(n):
    k, v = map(int, input().split())
    a.append((k, v))
a.sort(key=getKey)

s = [0]*len(a)
s[0] = a[0][1]
for index in range(1,len(a)):
    s[index] = s[index - 1] + a[index][1]

for i in range(m):
    l, r = map(int, input().split())
    l = find_l(l, a)
    r = find_r(r, a)
    # while k <= t:
    #     re += a[k][1]
    #     k += 1
    re = 0
    if l > r:
        print(0)
        continue
    if l > 0:
        re = s[r] - s[l - 1]
    else:
        re = s[r]
    print(re)



