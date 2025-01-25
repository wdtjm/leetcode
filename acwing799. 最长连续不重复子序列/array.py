def check(arr, s, i, j):
    k = j
    while k <= i:
        if s[arr[k]] > 1:
            return False
        k += 1
    return True


n = int(input())
arr = list(map(int, input().split()))
max_len = 0
j = 0
# 区间内的数
s = [0] * 100010

for i in range(len(arr)):
    s[arr[i]] += 1
    if s[arr[i]] <= 1:
        max_len = max(i - j + 1, max_len)
    else:
        while s[arr[i]] > 1:
            s[arr[j]] -= 1
            j += 1
print(max_len)
