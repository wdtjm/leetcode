n = int(input())


def bfs(t, n, s):
    # 剩t个，s,为字符串, n为范围
    if t == 0:
        print(' '.join(s))
    else:
        for i in range(1, n  + 1 ):
            if str(i) not in s:
                bfs(t-1, n, s + str(i))

bfs(n, n, '')
