class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodeToList(head):

    p = head
    lst = []
    #값만 리스트로 변경
    while p:
        lst.append(p.val)
        p = p.next

    #정렬
    lst.sort()

    p = head

    #노드에 정렬된 리스트 값 삽입
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head
    #끗

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

    result = nodeToList(head)
    print(f'result: {result}')
