def merge_sort(arr, l, r):
    if l >= r:
        return 0
    mid = (l + r) >> 1
    re = 0
    re += merge_sort(arr, l, mid) + merge_sort(arr, mid + 1, r)
    i, j, t = l, mid + 1, 0
    temp = []
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            re += mid + 1 - i
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
    while t <= r - l:
        arr[l+t] = temp[t]
        t += 1
    return re

# n = 6
# arr = [2, 3, 4, 5, 6, 1]
n = int(input())
arr = list(map(int, input().split()))
result = merge_sort(arr,0,n-1)
print(result)