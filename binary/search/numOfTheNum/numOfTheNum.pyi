def solution(x, lst):

    left = 0
    right = len(lst)-1

    last = -1
    first = -1

    def bin_search(x, lst):

        mid = (left + right)//2

        while left <= right:

            if x < lst[mid]:
                right = mid-1

            elif x > lst[mid]:
                left = mid+1

            else:
                if lst[mid+1] > x:
                        last = mid
                elif lst[mid-1] <x:
                        first = mid


    result = last - first


    return result

if __name__ == '__main__':

    x = int(input())
    lst = [1,1,2,2,2,2,3]

    result = solution(x, lst)

    print('result : ' + str(result))