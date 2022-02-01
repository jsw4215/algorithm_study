from bisect import bisect_left

def solution(n, l1, m, l2):

    result = []

    def bin_search():

        nonlocal result

        for x in l2:
            checker = False
            left = 0
            right = len(l1) - 1

            while left <= right:
                mid = (left + right) // 2

                if x > l1[mid]:
                    left = mid+1
                elif x < l1[mid]:
                    right = mid-1
                else:
                    if l1[mid] == x:
                        checker = True
                        break

            result.append(checker)

        return result

    l1.sort()


    result = bin_search()

    return result


if __name__ == '__main__':

    n = 5
    l1 = [8, 3, 7, 9, 2]
    m=3
    l2 = [5, 7, 9]

    result = solution(n, l1, m, l2)

    print('result : ' + str(result))