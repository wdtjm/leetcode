def quick_sort(arr,l,r):
    if( l>=r ):
        return
    i = l - 1
    j = r + 1
    x = arr[(l + r) >> 1]
    while i < j:
        i += 1
        while arr[i] < x:
            i += 1
        j -= 1
        while arr[j] > x:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, l, j)
    quick_sort(arr, j + 1, r)

if __name__ == '__main__':
    print("Hello World!")
    # n = int(input())
    # arr = list()
    n = 5
    arr = [2, 4, 5, 3, 1]
    # for i in range(n):
    #     arr.append(int(input()))
    quick_sort(arr,0,n-1)
    print(arr)

