class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeSort(head, tail, lv):

    #head가 tail을 넘어서기 전 까지 while 반복
    while head.next!=None:

        #mid node를 구한다
        #런너 기법 활용, slow는 한칸씩 나아가고, fast는 두칸씩 나아가서, fast가 tail에 도달할 때까지
        slow = head
        fast = head
        half = None
        while fast:
            slow = head.next
            fast = head.next.next
        half = slow

        print(f'{half}')



    pass


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

    result = mergeSort(head, node, 0)
    print(f'result: {result}')

