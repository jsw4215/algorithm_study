import copy
import sys
import bisect

def solution(inputList):

    inputList.reverse()

    inc_arr = [sys.maxsize]*n

    for i in range(0,n):
        idx = bisect.bisect_left(inc_arr, inputList[i])
        #해당 인덱스에 값을 덮어씀 => 총 길이가 증가하지 않음
        inc_arr[idx] = inputList[i]
    print(len(inputList) - bisect.bisect_left(inc_arr, sys.maxsize))

    pass


if __name__ == '__main__':


    n = int(input())
    inputList = list(map(int, input().split()))


    result = solution(inputList)
