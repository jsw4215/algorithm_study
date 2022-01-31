class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeNode(l1, l2):
    #l1이 더 크면 swap 다시 말해, 앞의 노드가 더 크면
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        #l1, l2가 연속된 단일노드가 아닌 경우
        l1.next = mergeNode(l1.next, l2)
    #l1 = Null, l2 = node 일 경우 l2 반환
    #l1 = node, l2 = node 일 경우 l1 반환
    #l1 = node, l2 = Null 일 경우 l1 반환
    return l1 or l2


def mergeSort(head):
    #head가 None이거나 head.next가 None인 경우 return head - 다시 말해 정렬할 것이 없다.
    if not (head and head.next):
        return head

    #mid node를 구한다
    #런너 기법 활용, slow는 한칸씩 나아가고, fast는 두칸씩 나아가서, fast가 tail에 도달할 때까지
    slow = head
    fast = head
    mid = None
    # head가 tail을 넘어서기 전 까지 while 반복
    while fast and fast.next:
        mid = slow
        slow = slow.next
        fast = fast.next.next
    mid.next = None

    l1 = mergeSort(head)
    l2 = mergeSort(slow)

    result = mergeNode(l1, l2)

    return result


if __name__ == '__main__':

    dummy = [4, 2, 1, 3]

    for i in reversed(range(len(dummy))):
        if i + 1 != len(dummy):
            node = ListNode(dummy[i], node)
        else:
            node = ListNode(i, None)

    head = node
    for _ in range(len(dummy)-1):
        node = node.next

    result = mergeSort(head)
    print(f'result: {result}')

