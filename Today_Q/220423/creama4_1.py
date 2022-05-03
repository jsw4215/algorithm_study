def subSet(inputNum):   
   
    result = []
    prev_elements = []
    next_elements = []

    def dfs(elements):

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            prev_elements.sort()

            if prev_elements not in result:
                result.append(prev_elements[:])
            dfs(next_elements)
            elements.pop(0)
            prev_elements.pop()

    dfs(inputNum)

    return result

def solution(arr, k):

    result = 0
    arr.sort()

    def bin_search(left, right):

        nonlocal result

        while left < right:
            
            mid = (left + right) // 2
            print("mid",mid)

            temp = sum(arr[:mid])

            if temp <= k:
                left = mid+1
                result = mid
            elif temp > k:
                right = mid-1

    left = 0
    right = len(arr)

    bin_search(left, right)
    print("result", result)
    return result

if __name__ == '__main__':

    n = [3,1,2,1]
    k = 4
    palinList = solution(n, k)