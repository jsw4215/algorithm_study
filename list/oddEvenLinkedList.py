class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenLL(head: ListNode):

    if head is None:
        return None

    headForReturn = head
    secondStartingPoint = head.next
    secondCurr = secondStartingPoint

    curr = head

    while curr is not None:

        temp = curr.next

        if curr.next is not None:
            curr.next = curr.next.next
            secondCurr.next = temp
            secondCurr = secondCurr.next
            secondCurr.next = None
        else:
            curr.next = secondStartingPoint
            break
        if curr.next is not None:
            curr = curr.next

    return headForReturn


if __name__ == '__main__':

    fifth_node = ListNode(5,None)
    fourth_node = ListNode(4,fifth_node)
    third_node = ListNode(3,fourth_node)
    second_node = ListNode(2,third_node)
    first_node = ListNode(1,second_node)

    result = oddEvenLL(first_node)

    while (True):
        print('result : ' + str(result.val))
        if result.next is None:
            break
        result = result.next
