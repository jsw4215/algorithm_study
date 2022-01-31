class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def partition(head, tail):
    # if head.next is None:
    #     return head

    pivot = tail.val

    iNode = ListNode()
    iNode.next = head

    cur = head

    while cur is not tail:
        if cur.val <= pivot:
            iNode = iNode.next
            iNode.val, cur.val = cur.val, iNode.val
        cur = cur.next

    iNode.next.val, tail.val = tail.val, iNode.next.val

    return iNode


def nodeQuickSort(head, tail, lv):
    # if head is None or head.next is None or head is tail:
    #     return head

    prevPivot = partition(head, tail)

    if prevPivot.val is None:
        return head

    if head is prevPivot:
        return head

    nodeQuickSort(head, prevPivot, lv+1)

    if prevPivot.next.next is tail or prevPivot.next is tail:
        return head

    nodeQuickSort(prevPivot.next.next, tail, lv+1)

    return head


if __name__ == '__main__':

    dummy = [4, 2, 1, 5, 3]

    for i in reversed(range(len(dummy))):
        if i + 1 != len(dummy):
            node = ListNode(dummy[i], node)
        else:
            node = ListNode(dummy[i], None)

    head = node

    # 꼬리노드 구하기
    tail = head
    while tail.next is not None:
        tail = tail.next

    result = nodeQuickSort(head, tail, 0)

    while True:
        if result.next is not None:
            print(f'{result.val}->', end="")
            result = result.next

        else:
            print(f'{result.val}', end="")
            break


