class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLL(head: ListNode):
    curr = head
    print('head : ' + str(head.val))
    prev = None

    while curr is not None:
        print('curr : ' + str(curr.val) + ', curr.next : ' + str(curr.next))
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


if __name__ == '__main__':

    fifth_node = ListNode(5,None)
    fourth_node = ListNode(4,fifth_node)
    third_node = ListNode(3,fourth_node)
    second_node = ListNode(2,third_node)
    first_node = ListNode(1,second_node)

    result = reverseLL(first_node)

    while (True):
        print('result : ' + str(result.val))
        result = result.next
