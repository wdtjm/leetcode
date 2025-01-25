class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, value):
        h = self.head
        if h is None:
            self.head = [None, value]
            self.length += 1
            return
        while h[0] is not None:
            h = h[0]
        h[0] = [None, value]
        self.length += 1

    def insert(self, p, v):
        if p > self.length:
            return -1
        if p == 0:
            self.head = [None, v]
            self.length += 1
            return
        h = self.head
        for i in range(p - 1):
            h = h[0]
        h[0] = [h[0], v]

    def __str__(self):
        h = self.head
        s = ''
        while h is not None:
            s += str(h[1]) + ' '
            h = h[0]
        return s.strip()


ll = LinkedList()
ll.insert(0,1)
ll.insert(1, 2)
print(ll)