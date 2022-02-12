import sys, bisect

with open('LIS_testcase.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    inc_arr = [sys.maxsize]*n

    for i in range(0,n):
        idx = bisect.bisect_left(inc_arr, arr[i])
        #해당 인덱스에 값을 덮어씀 => 총 길이가 증가하지 않음
        inc_arr[idx] = arr[i]
    print(bisect.bisect_left(inc_arr, sys.maxsize))