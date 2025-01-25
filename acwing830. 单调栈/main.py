n = int(input())
arr = list(map(int, input().split()))
st = []
ans = []
for i in range(len(arr)):
    while st and arr[st[-1]] >= arr[i]:
        st.pop()
    if st:
        ans.append(arr[st[-1]])
    else:
        ans.append(-1)
    st.append(i)
print(' '.join(map(str, ans)))

'''
输入样例：
5
3 4 2 7 5
输出样例：
-1 3 -1 2 2


'''