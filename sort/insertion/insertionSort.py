class PracSort():
    def __init__(self):
        self.items=[]

    def insertionSort(self, l):

        for i in range(1,len(l)):
            key = l[i]
            j = i-1
            while j>=0 :
                if l[j] > key:
                    l[j+1] = l[j]
                    l[j] = key
                j-=1

        return l

    def bubbleSort(self, l):

        for i in range(len(l)-1):
            for j in range(len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]

        return l

    def selectionSort(self, l):

        for i in range(len(l)-1):
            min = i
            for j in range(i+1,len(l)):
                if l[min] > l[j]:
                    min = j
            l[min], l[i] = l[i], l[min]


        return l


if __name__ == '__main__':

    dummy = [6,3,5,8,9,5,45,123,569]

    sorting = PracSort()

    l = sorting.selectionSort(dummy)

    print(f'{l}')