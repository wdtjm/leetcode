n, m = map(int, input().split())
arr = list(map(int, input().split()))
length = 0
h = [0] * (n + 1)
def insert(val):
    global length, arr, h
    h[length + 1] = val
    p = length + 1
    while p > 1 and h[p] < h[p//2]:
        t = h[p]
        h[p] = h[p//2]
        h[p//2] = t
        p //= 2
    length += 1


def pop():
    global length, h
    if length == 0:
        return
    min = h[1]
    h[1] = h[length]
    length -= 1
    p = 1
    while not (p*2 > length or (h[p] < h[p*2] and h[p] < h[p*2 + 1 if p*2 + 1 <= length else p * 2] )):
        if p*2 == length:
            swap_p = p * 2
        else:
            if h[p*2] > h[p*2 + 1]:
                swap_p = p*2 + 1
            else:
                swap_p = p*2
        t = h[swap_p]
        h[swap_p] = h[p]
        h[p] = t
        p = swap_p
    return min


ans = []
for i in range(n):
    insert(arr[i])
for i in range(m):
    ans.append(pop())
print(' '.join(list(map(str, ans))))