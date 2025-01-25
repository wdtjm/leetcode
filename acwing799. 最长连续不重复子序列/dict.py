def check(arr, s, i, j):
    k = j
    while k <= i:
        if s.get(str(arr[k]), 0) > 1:
            return False
        k += 1
    return True


n = int(input())
arr = list(map(int, input().split()))
max_len = 0
j = 0
# 区间内的数
s = dict()

for i in range(len(arr)):
    if s.get(str(arr[i]), None) is None:
        s[str(arr[i])] = 1
    else:
        s[str(arr[i])] += 1
    if check(arr, s, i, j):
        max_len = max(i - j + 1, max_len)
    else:
        s[str(arr[j])] -= 1
        j += 1
print(max_len)
