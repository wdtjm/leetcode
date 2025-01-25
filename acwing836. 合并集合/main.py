n, m = map(int, input().split())

arr = [0] * (n + 1)

for i in range(m):
    args = input().split()
    a, b = int(args[1]), int(args[2])
    if args[0] == 'M':
         root_a, root_b = a, b
         len_a, len_b = 0, 0
         while arr[root_a] != 0:
             root_a = arr[root_a]
             len_a += 1
         while arr[root_b] != 0:
             root_b = arr[root_b]
             len_b += 1
         if root_a != root_b:
             if len_a < len_b:
                arr[root_a] = root_b
             else:
                arr[root_b] = root_a
    else:
        root_a, root_b = a, b
        while arr[root_a] != 0:
            root_a = arr[root_a]
        while arr[root_b] != 0:
            root_b = arr[root_b]
        if root_a == root_b:
            print("Yes")
        else:
            print("No")
