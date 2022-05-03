from collections import deque


def solution(data):

    data.sort(reverse=True)

    print(data)

    group = 0

    while data:
        x = data.pop()
        for _ in range(x-1):
            if(len(data)==0):
                break
            data.pop()
        else:
            #for문을 다 돌았을때만 들어옴    
            group+=1
    
    print("res",group)
    return group


if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))

    palinList = solution(data)