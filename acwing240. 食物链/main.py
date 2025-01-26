n, k = map(int, input().split())
arr = [0] * (n + 1)
d = [0] * (n + 1)
num = 0


def find(x):
    # 找到根节点
    if arr[x] == 0:
        return x
    else:
        return find(arr[x])


def isConflict(x, y):
    # x 吃
    # 关系 C3 -> A2 -> B1 -> C0
    # x 吃 y => d[x] - d[y] % 3 = 1
    # x 与 y 同类 => d[x] - d[y] % 3 = 0
    if find(x) == find(y) and (getDistance(x, y) % 3 != 1):
        return True
    else:
        return False


def getDistance(x, y):
    if find(x) != find(y):
        return 0
    else:
        def getDfromRoot(x):
            if arr[x] != 0:
                return d[x] + getDfromRoot(arr[x])
            else:
                return 0
        return getDfromRoot(x) - getDfromRoot(y)


def notSameType(x, y):
    if find(x) == find(y) and (getDistance(x, y) % 3 != 0):
        return True
    else:
        return False


for i in range(k):
    o, x, y = input().split()
    x, y = int(x), int(y)
    if o == '1':
        if x > n or y > n:
            num += 1
        else:
            # 判断是否与以前的话冲突: x y 是同类
            if notSameType(x, y):
                num += 1
            elif arr[y] == 0:
                arr[x] = y
                d[x] = 0
            else:
                arr[y] = x
                d[y] = 0
    else:
        if x > n or y > n:
            num += 1
            # x 吃 y
        elif isConflict(x, y):
            num += 1
        elif arr[y] == 0:
            arr[x] = y
            d[x] = 1
        else:
            arr[y] = x
            d[y] = 1
print(num)