class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.isNum = False


root = Node()
n = int(input())


def getBin(num: str) -> str:
    return bin(int(num))[2:].zfill(31)


arr = list(map(getBin, input().split()))
# binary = format(10, '32b') 输出10的32位二进制字符

# 将二进制字符插入树中
for word in arr:
    # 对于每个arr中的二进制数字字符串，将其插入前缀树中
    cur = root
    for char in word:
        if char == '0':
            if cur.left is None:
                cur.left = Node()
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node()
            cur = cur.right
    cur.isNum = True


def getNotOrValue(num):
    # num是二进制字符
    cur = root
    re = ""
    for char in num:
        if char == '1':
            if cur.left is not None:
                re += '1'
                cur = cur.left
            else:
                re += '0'
                cur = cur.right
        else:
            if cur.right is not None:
                re += '1'
                cur = cur.right
            else:
                re += '0'
                cur = cur.left
    return int(re, 2)


arr = list(map(getNotOrValue, arr))
print(max(arr))
