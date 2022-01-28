import sys

class PracticeMinHeap:

    def __init__(self):
        self.items=[None]

    def __len__(self):
        return len(self.items)-1

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        root = self.items.pop()
        self.percolate_down(1)

        return root

    def percolate_down(self, k):

        cur = k

        left = 2*k
        right = 2*k+1

        if left <= len(self) and self.items[cur] > self.items[left]:
            self.items[cur], self.items[left] = self.items[left], self.items[cur]
            cur = left

        if right <= len(self) and self.items[cur] > self.items[right]:
            self.items[cur], self.items[right] = self.items[right], self.items[cur]
            cur = right

        if cur != k:
            self.percolate_down(cur)


    def percolate_up(self):

        cur = len(self)

        parents = cur//2

        while parents > 0:

            if self.items[cur] < self.items[parents]:
                self.items[cur], self.items[parents] = self.items[parents], self.items[cur]

            cur = parents
            parents = cur//2

if __name__ == '__main__':

    number = int(input())
    heap = []

    test = PracticeMinHeap()

    for i in range(number):
        num = int(sys.stdin.readline())
        if num==0:
            temp = test.extract()
            if temp is None:
                print('0')
            else:
                print(temp)
        else:
            test.insert(num)