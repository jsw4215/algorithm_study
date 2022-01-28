class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSort(head):

    cur = parent = ListNode(None)

    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next,head.next,head = head,cur.next,head.next

        cur = parent

    return cur.next

if __name__ == '__main__':
    dummy = [4,2,1,3]

    for i in reversed(range(len(dummy))):
        if i+1 != len(dummy):
            node = ListNode(dummy[i],node)
        else:
            node = ListNode(i, None)

    sorted = insertionSort(node)

    print(f'{sorted}')
