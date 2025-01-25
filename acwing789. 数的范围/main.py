def divide_querry(arr, l, r, m):
    i, j = l-1, r+1
    result = [-1, -1]
    # 先找左边界
    while i + 1 != j:
        mid = (i + j) >> 1
        if arr[mid] < m:
            i = mid
        else:
            j = mid
    if j <= r and arr[j] == m:
        result[0] = j
    i, j = l-1, r+1
    # 找右边界
    while i + 1 != j:
        mid = (i + j) >> 1
        if arr[mid] <= m:
            i = mid
        else:
            j = mid
    if i >= l and arr[i] == m:
        result[1] = i
    return result


# n, q = 6, 3
# arr = [1, 2, 2, 3, 3, 4]
# q_arr = [3, 4, 5]
n, q = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
q_arr = []
while i < q:
    q_arr.append(int(input()))
    i += 1
for i in q_arr:
    print(' '.join(list(map(str,divide_querry(arr, 0, n-1, i)))))
