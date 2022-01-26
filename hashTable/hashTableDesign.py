import collections

from list.oddEvenLinkedList import ListNode


class MyHashMap:
    #초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    #삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        #인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        #인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
                p=p.next
            p.next = ListNode(key, value)





