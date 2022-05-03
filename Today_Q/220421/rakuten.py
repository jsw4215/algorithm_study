from collections import Counter

def solution(arr, k):

    n=len(arr)
    arr.sort()
    counter = Counter(arr)
    몫, 나머지 = divmod(k - 1, n)
    if counter[arr[몫]] > 1:
        index = arr.index(arr[몫])  #중복 중에 제일 처음 요소의 위치
        차이 = 몫 - index
        x = 차이 * n + 나머지
        몫2 = x // counter[arr[몫]]
        return [arr[몫], arr[몫2]]
        
    else:
        return [arr[몫], arr[나머지]]

if __name__ == '__main__':

    arr = [2,2,1]

    k = 5

    result = solution(arr,k)

    print(str(result))