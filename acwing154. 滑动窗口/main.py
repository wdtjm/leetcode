from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_d = deque()
min_d = deque()
ans = []
min_ans = []
for i in range(k - 1):
    while len(max_d) != 0 and arr[max_d[-1]] <= arr[i]:
        max_d.pop()
    max_d.append(i)
    while len(min_d) != 0 and arr[min_d[-1]] >= arr[i]:
        min_d.pop()
    min_d.append(i)

for i in range(k - 1, n):
    while max_d and arr[max_d[-1]] <= arr[i]:
        max_d.pop()
    max_d.append(i)
    ans.append(arr[max_d[0]])
    if max_d[0] <= i - k + 1:
        max_d.popleft()

    while min_d and arr[min_d[-1]] >= arr[i]:
        min_d.pop()
    min_d.append(i)
    min_ans.append(arr[min_d[0]])
    if min_d[0] <= i - k + 1:
        min_d.popleft()
print(' '.join(list(map(str, min_ans))))

print(' '.join(list(map(str, ans))))
'''
核心思路：丢弃掉不可能的值
比如 3 1 4 2
4前面的值不可能为最大值
1前面的值不可能为最小值
'''