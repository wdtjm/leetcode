from collections import deque

m = int(input())
d = deque()
for i in range(m):
    operation = list(input().split())
    if operation[0] == "push":
        d.append(int(operation[1]))
    elif operation[0] == "pop":
        d.popleft()
    elif operation[0] == "empty":
        if len(d) == 0:
            print("YES")
        else:
            print("NO")
    elif operation[0] == "query":
        i = d.popleft()
        d.appendleft(i)
        print(i)
