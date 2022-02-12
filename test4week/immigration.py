def solution(n, times):

    result = 0


    def bin_search():

        left = 1
        right = max(times)*n


        while left <= right:
            nonlocal result
            people = 0
            mid = (left + right)//2

            for time in times:
                people += mid // time

            if n <= people:
                right = mid-1
                result = mid
            elif n > people:
                left = mid+1
            else:
                break

    bin_search()

    return result


if __name__ == '__main__':

    n = 6
    times = [7,10]

    result = solution(n, times)

    print('result : ' + str(result))

