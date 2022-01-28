class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_with_sort(list1: ListNode, list2: ListNode):

    list = []

    curr = list1
    curr2 = list2

    while True:

        if curr is None:
            list.append(curr2.val)
            curr2=curr2.next
        elif curr2 is None:
            list.append(curr.val)
            curr=curr.next
        elif curr.val == curr2.val :
            list.append(curr.val)
            list.append(curr2.val)
            curr=curr.next
            curr2=curr2.next
        elif curr.val < curr2.val :
            list.append(curr.val)
            curr=curr.next
        else :
            list.append(curr2.val)
            curr2=curr2.next

        if curr is None and curr2 is None:
            break

    return list


if __name__ == '__main__':

    arr2_third_node = ListNode(4, None)
    arr2_second_node = ListNode(3, arr2_third_node)
    arr2_first_node = ListNode(1, arr2_second_node)

    arr1_third_node = ListNode(3,None)
    arr1_second_node = ListNode(2,arr1_third_node)
    arr1_first_node = ListNode(1,arr1_second_node)

    result = merge_with_sort(arr1_first_node, arr2_first_node)

    print('result : ' + str(result))
