def getKey(item):
    return item[0]


n = int(input())
a = []
for i in range(n):
    l, r = map(int, input().split())
    a.append((l, r))
a.sort(key=getKey)
result = []
if len(a) == 1:
    print("1")
else:
    i = 1
    j = 0
    result.append(a[0])
    while i < len(a):
        if result[j][0] <= a[i][0] <= result[j][1]:
            result[j] = (result[j][0], max(a[i][1], result[j][1]))
            i += 1
        else:
            result.append(a[i])
            i += 1
            j += 1
    print(len(result))

'''
注意

不能在原来的数组中合并区间，在数组中合并区间涉及删除数组中元素这一操作，耗时较长，直接开辟一个新的数组来储存结果区间

用list而不是tuple来存区间更合理
'''