class root:
    def __init__(self):
        self.size = 1


n, m = map(int, input().split())
arr = [root() for i in range(n + 1)]
for i in range(m):
    args = input().split()
    if args[0] == 'C':
        a, b = int(args[1]), int(args[2])
        root_a, root_b = a, b
        while arr[root_a].__class__ != root:
            root_a = arr[root_a]
        while arr[root_b].__class__ != root:
            root_b = arr[root_b]
        if root_a != root_b:
            if arr[root_a].size > arr[root_b].size:
                arr[root_a].size += arr[root_b].size
                arr[root_b] = root_a
            else:
                arr[root_b].size += arr[root_a].size
                arr[root_a] = root_b
    elif args[0] == "Q1":
        a, b = int(args[1]), int(args[2])
        root_a, root_b = a, b
        while arr[root_a].__class__ != root:
            root_a = arr[root_a]
        while arr[root_b].__class__ != root:
            root_b = arr[root_b]
        if root_a != root_b:
            print("No")
        else:
            print("Yes")
    elif args[0] == "Q2":
        a = int(args[1])
        root_a = a
        while arr[root_a].__class__ != root:
            root_a = arr[root_a]
        print(arr[root_a].size)
'''
bug:
arr = [root()] * (n + 1)
原因：
这样得到的数值中root的地址指向的是同一份
正确做法：
arr = [root() for i in range(n + 1)]
'''
