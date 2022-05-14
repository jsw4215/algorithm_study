import sys

def solution():
    volume = 0
    stack = []

    for i in range(len(height)):
        #상승세에선 빗물 volume 더해주기
        while stack and height[i] > height[stack[-1]]:
            btm = height[stack.pop()]
            
            #맨 처음엔 이전의 벽이 존재하지 않음
            if not len(stack):
                break
            
            top = min(height[stack[-1]], height[i])
            width = i - stack[-1] - 1
            h = top - btm
            volume += width * h
        
        #하락세에선 append만
        stack.append(i)
    return volume

if __name__ == '__main__':

    h, w = map(int, sys.stdin.readline().split())

    height = list(map(int, sys.stdin.readline().split()))

    res = solution()

    print(res)