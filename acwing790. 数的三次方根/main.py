def three_root(n, l, r):
    i, j = l, r
    re = mid = (i + j)/2
    while abs(re*re*re - n) > 1e-9:
        if re*re*re - n > 0:
            j = re
            re = (i + j)/2
        elif re*re*re - n == 0:
            return re
        else:
            i = re
            re = (i + j)/2
    return re


n = float(input())
print('{:.6f}'.format(three_root(n, -50, 50)))
