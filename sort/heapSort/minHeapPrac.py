class MinHeapPrac:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) -1

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()


    def extract(self):
        if len(self) < 1:
            return None

        self.items[-1], self.items[1] = self.items[1], self.items[-1]
        temp = self.items.pop()
        self._percolate_down(1)
        return temp


    def _percolate_up(self):

        cur = len(self.items)

        parents = cur // 2

        while parents > 0:

            if self.items[cur] < self.items[parents]:
                #swap
                self.items[cur], self.items[parents] = self.items[parents], self.items[cur]

                cur = parents
                parents = cur//2


    def _percolate_down(self, k):

        cur = k

        left = 2*k
        right = 2*k+1

        if left < len(self) and self.items[cur] > self.items[left]:
            self.items[cur], self.items[left] = self.items[left], self.items[cur]
            cur = left

        if right < len(self) and self.items[cur] > self.items[right]:
            self.items[cur], self.items[right] = self.items[right], self.items[right]
            cur = right

        if cur!=k:
            self._percolate_down(cur)







