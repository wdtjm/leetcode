N = 100010
# ph pointer to heap, ph[k] = index 第k次插入的元素在heap中下标为index
# hp heap to pointer, hp[index] = k, heap中下标为index的元素是第k次插入的
ph = [0] * N
hp = [0] * N

heap = [0] * N
length = 0


def swap(index1, index2):
    ph[hp[index1]], ph[hp[index2]] = index2, index1
    hp[index1], hp[index2] = hp[index2], hp[index1]
    heap[index1], heap[index2] = heap[index2], heap[index1]


def up(index):
    while (index // 2) > 0 and heap[index] < heap[index//2]:
        swap(index, index//2)
        index //= 2


# def down(index):
#     while (index*2 < length) and (heap[index] < heap[index*2] or heap[index] < heap[index*2 + 1 if index*2  +1 < length else index*2]):
#         if index*2 == length or heap[index*2] < heap[index*2  + 1]:
#             swap(index, index*2)
#             index = index*2
#         else:
#             swap(index, index*2 + 1)
#             index = index*2  +1


def down(index):
    while True:
        smallest = index
        if index * 2 <= length and heap[index * 2] < heap[smallest]:
            smallest = index * 2
        if index * 2 + 1 <= length and heap[index * 2 + 1] < heap[smallest]:
            smallest = index * 2 + 1
        if smallest != index:
            swap(index, smallest)
            index = smallest
        else:
            break


n = int(input())
insert_count = 0
for i in range(n):
    args = input().split()
    if args[0] == "I":
        insert_count += 1
        length += 1
        heap[length] = int(args[1])
        hp[length] = insert_count
        ph[insert_count] = length
        up(length)
    elif args[0] == "PM":
        print(heap[1])
    elif args[0] == "DM":
        swap(1, length)
        length -= 1
        down(1)
    elif args[0] == "D":
        k = int(args[1])
        index = ph[k]
        swap(ph[k], length)
        length -= 1
        up(index)
        down(index)
    elif args[0] == "C":
        k, x = int(args[1]), int(args[2])
        heap[ph[k]] = x
        up(ph[k])
        down(ph[k])