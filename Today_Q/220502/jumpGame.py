from collections import deque
import sys

def solution(n):

    pointer = [0,0,0]
    
    def bfs(ptr):
        q = deque([ptr])

        while q:
            t, *ptr = q.popleft()
            
            t+=1

            onePtr = [ptr[0], ptr[1]+1]
            twoPtr = [abs(ptr[0]-1), ptr[1]+k]
            threePtr = [ptr[0], ptr[1]-1]

            if onePtr[1]>=n:
                    return 1
            if tot[onePtr[0]][onePtr[1]]=='1' and onePtr[1]>=t:
                tot[onePtr[0]][onePtr[1]]= '0'
                q.append([t,onePtr[0],onePtr[1]])
            
            if twoPtr[1]>=n:
                return 1
            if tot[twoPtr[0]][twoPtr[1]]=='1' and twoPtr[1]>=t:
                tot[twoPtr[0]][twoPtr[1]]= '0'
                q.append([t,twoPtr[0],twoPtr[1]])

            if threePtr[1]>=n:
                return 1
            if tot[threePtr[0]][threePtr[1]]=='1' and threePtr[1]>=t:
                tot[threePtr[0]][threePtr[1]]= '0'
                q.append([t,threePtr[0],threePtr[1]])

        return 0

    res = bfs(pointer)

    return res

if __name__ == '__main__':
    
    input = sys.stdin.readline

    n, k = map(int, input().split())

    left = input()
    right = input()

    tot = deque([list(left), list(right)])

    res = solution(n)

    print(res)