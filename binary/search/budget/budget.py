def solution(n, lst, tot):
    result = 0

    def tot_budget(mid):
        temp = 0
        for i in lst:
            if i <= mid:
                temp += i
            elif i > mid:
                temp += mid

        return temp


    def bin_search():

        left = 0
        right = max(lst)

        while left <= right:
            nonlocal result

            mid = (left + right)//2

            total = tot_budget(mid)

            if total > tot:
                right = mid-1
            elif total < tot:
                left = mid+1
                result = mid
            else:
                result = mid
                break
        return mid

    bin_search()


    return result

if __name__ == '__main__':

    n = int(input())

    lst = list(map(int, input().split()))

    tot = int(input())

    result = solution(n, lst, tot)

    print(f'{result}')
