n, m = map(int, input().split())
a = input()
b = 29
mod = 2 ** 64

# 预先计算所有可能的幂次
pow_b = [1] * (len(a) + 1)
for i in range(1, len(a) + 1):
    pow_b[i] = (pow_b[i - 1] * b) % mod

def getHash(l, r):
    # re = 0
    # for i in range(l-1, r):
    #     re *= b
    #     re += ord(a[i])
    # return re
    return  (s[r] - s[l - 1]*pow_b[r - l + 1])%mod


s = [0]*(len(a) + 1)
for i in range(len(a)):
    s[i + 1] = (s[i]*b + ord(a[i]))%mod

for i in range(m):
    l1, r1, l2, r2 = map(int, input().split())
    if getHash(l1, r1) == getHash(l2, r2):
        print("Yes")
    else:
        print("No")
