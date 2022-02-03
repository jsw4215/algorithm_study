#반례가 어려운 문제
#개수를 얻었다고 해서 끝나는게 아니라,
#1 1
#2147483647
#입력시에도 값이 나와야한다.
#답은 2147483647
#
#left를 0으로 시작시,
#5 5
#1
#1
#1
#1
#1
#이걸 통과할 수 없다.

def solution(n, m, lst):

    result = 0

    def tot_tree_get(mid):
        temp = 0
        for i in lst:
            temp += (i // mid)

        return temp


    def bin_search():

        left = 1
        right = max(lst)

        while left <= right:
            nonlocal result

            mid = (left + right)//2

            total = tot_tree_get(mid)

            if total >= m:
                left = mid+1
                result = mid
            elif total < m:
                right = mid-1
        return mid

    bin_search()

    return result

if __name__ == '__main__':

    n, m = map(int, input().split())

    lst = []

    for _ in range(n):
        temp = int(input())
        lst.append(temp)

    result = solution(n, m, lst)

    print(f'{result}')
