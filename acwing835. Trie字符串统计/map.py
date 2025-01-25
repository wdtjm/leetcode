n = int(input())
d = dict()
for i in range(n):
    args = input().split()
    if args[0] == 'I':
        if d.get(args[1]) is None:
            d[args[1]] = 1
        else:
            d[args[1]] += 1
    else:
        if d.get(args[1]) is None:
            print('0')
        else:
            print(str(d[args[1]]))
