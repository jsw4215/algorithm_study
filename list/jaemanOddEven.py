class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEven(head: ListNode):
    curr = head
    evens = []

    while curr is not None:
        if (curr.next).next :
            evens.append(curr.next)
            curr.next = (curr.next).next
            curr = (curr.next).next
        elif len(evens) == 0:
            break
        else:
            even = evens.pop(0)
            curr.next = even
            curr = even
            even.next = None
        print(curr)


if __name__ == '__main__':

    fifth_node = ListNode(5,None)
    fourth_node = ListNode(4,fifth_node)
    third_node = ListNode(3,fourth_node)
    second_node = ListNode(2,third_node)
    first_node = ListNode(1,second_node)

    result = oddEven(first_node)

    print(result)