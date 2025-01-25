def merge_sort(arr, l, r):
    if r - l <= 0:
        return
    mid = (l + r) >> 1
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)
    tem = []
    i, j, p = l, mid+1, l
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            tem.append(arr[i])
            i += 1
        else:
            tem.append(arr[j])
            j += 1
    while i <= mid:
        tem.append(arr[i])
        i += 1
    while j <= r:
        tem.append(arr[j])
        j += 1
    i = 0
    while i <= r-l:
        arr[l+i] = tem[i]
        i += 1
    return


# n = int(input())
# arr = list(map(int, input().split()))
# n = 5
# arr = [2, 4, 5, 3, 1]
n = 10
arr = [99, 51, 84, 48, 76, 42, 6, 6, 38, 10]
merge_sort(arr,0,n-1)
print(' '.join(list(map(str,arr))))
