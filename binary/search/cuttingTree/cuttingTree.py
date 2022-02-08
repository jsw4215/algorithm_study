def solution(n, m, lst):

    result = 0

    def tot_tree_get(mid):
        temp = 0
        for i in lst:
            if i > mid:
                temp += (i - mid)

        return temp


    def bin_search():

        left = 0
        right = max(lst)

        while left <= right:
            nonlocal result

            mid = (left + right)//2

            total = tot_tree_get(mid)

            if total > m:
                left = mid+1
                result = mid
            elif total < m:
                right = mid-1
            else:
                result = mid
                break
        return mid

    bin_search()


    return result

if __name__ == '__main__':

    n, m = map(int, input().split())

    lst = list(map(int, input().split()))

    result = solution(n, m, lst)

    print(f'{result}')
