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
    while True:
        smallest = p
        if p*2 <= length and h[smallest] > h[p*2]:
            smallest = p*2
        if p*2 + 1 <= length and h[smallest] > h[p*2 + 1]:
            smallest = p*2 + 1
        if smallest == p:
            break
        else:
            t = h[smallest]
            h[smallest] = h[p]
            h[p] = t
            p = smallest
    return min


ans = []
for i in range(n):
    insert(arr[i])
for i in range(m):
    ans.append(pop())
print(' '.join(list(map(str, ans))))