def solution(n, num, operator):
    result = []
    next_nodes = []
    prev_nodes = []
    ee = []
    _min = int(1e9)
    _max = -int(1e9)

    def cal(operator):
        nonlocal _max
        nonlocal _min
        temp = num[0]

        for i in range(n - 1):
            if operator[i] == 0:
                # 더하기
                temp += num[i+1]
            elif operator[i] == 1:
                # 빼기
                temp -= num[i+1]
            elif operator[i] == 2:
                # 곱하기
                temp *= num[i+1]
            elif operator[i] == 3:
                # 나누기
                if temp<0:
                    temp=-temp
                    temp//=num[i+1]
                    temp=-temp
                temp //= num[i+1]

        _max = max(_max, temp)
        _min = min(_min, temp)


    def dfsFunc(operators):
        if sum(operators) == 0:
            ee.append(prev_nodes[:])
            cal(prev_nodes)


        for idx, node in enumerate(operators):
            if node==0:
                continue

            next_nodes = operators[:]
            next_nodes[idx]-=1

            prev_nodes.append(idx)
            dfsFunc(next_nodes)
            prev_nodes.pop()

    dfsFunc(operator)

    print(_max)
    print(_min)


if __name__ == '__main__':
    N = int(input())

    nums = list(map(int, input().split()))

    operator = list(map(int, input().split()))

    solution(N, nums, operator)

# 2
# -9 3
# 0 0 0 1