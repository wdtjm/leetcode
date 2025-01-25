trie = [None,[]]
# 第一个元素存有本节点代表的字母，第二个列表存有指向下级节点的指针
n = int(input())
class Node:
    def __init__(self):
        self.sons = dict()
        self.isLeaf = False
        self.sum = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word) -> None:
        cur = self.root
        for c in word:
            if cur.sons.get(c) is None:
                cur.sons[c] = Node()
            cur = cur.sons[c]
        cur.isLeaf = True
        cur.sum += 1

    def prefix(self, word) -> int:
        cur = self.root
        for c in word:
            if cur.sons.get(c) is None:
                return 0
            cur = cur.sons[c]

        def dfs(node) -> int:
            re = 0
            if node.isLeaf:
                re += 1
            for t in node.sons:
                re += dfs(node.sons[t])
            return re
        return dfs(cur)

    def sum(self, word) -> int:
        cur = self.root
        for c in word:
            if cur.sons.get(c) is None:
                return 0
            cur = cur.sons[c]
        return cur.sum

trie = Trie()
for i in range(n):
    args = input().split()
    if args[0] == 'I':
        trie.insert(args[1])
    else:
        print(trie.sum(args[1]))

