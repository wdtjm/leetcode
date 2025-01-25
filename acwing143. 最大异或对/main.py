class Node:
    def __init__(self):
        self.sons = dict()
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
        if cur.sons.get(char) is None:
            cur.sons[char] = Node()
        cur = cur.sons[char]
    cur.isNum = True

def logicNot(o):
    if o == '1':
        return '0'
    else:
        return '1'

def getNotOrValue(num):
    # num是二进制字符
    cur = root
    re = ""
    for char in num:
        if cur.sons.get(logicNot(char)) is None:
            cur = cur.sons[char]
            re += '0'
        else:
            re += '1'
            cur = cur.sons[logicNot(char)]
    return int(re, 2)

arr = list(map(getNotOrValue, arr))
print(max(arr))
