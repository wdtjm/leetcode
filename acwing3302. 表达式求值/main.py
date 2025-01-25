from collections import deque

a = input().split()
origin = deque(a)
operators = deque()

while len(origin) != 0:
    i = origin.pop()
    if i == '+' or i == '-' or i == ')':
        a = 1
