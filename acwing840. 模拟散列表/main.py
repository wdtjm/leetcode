n = int(input())

N = 100000

arr = [[] for i in range(N)]


def hashCode(val):
    return val % N


for i in range(n):
    args = input().split()
    val = int(args[1])
    if args[0] == "Q":
        if arr[hashCode(val)].count(val) == 0:
            print("No")
        else:
            print("Yes")
    else:
        arr[hashCode(val)].append(val)