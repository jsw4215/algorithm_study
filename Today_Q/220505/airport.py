from collections import deque
import sys

def find_parent(x):
    if parent[x] == x:
        return x
    P = find_parent(parent[x])
    parent[x] = P
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
def solution():

    #1. 항공기가 도착했을 때, 해당 게이트에 연결한다.
    #2. 이미 도킹이 되어있다면, 번호가 낮은 게이트에 연결한다.
    #3. 부모가 이미 도킹되어있다면, 다음 번호로 넘어가며 업데이트해둔다.
    
    cnt = 0
    while airPlane:
        
        gate = airPlane.popleft()
        #부모 확인 후 게이트 할당받기
        emptyGate = find_parent(gate)

        if emptyGate==0:
            break

        cnt+=1
        #게이트 비어있는지 확인하고 비었으면 넣기, 넣고 parent-=1
        union(emptyGate, emptyGate-1)

    return cnt

if __name__ == '__main__':

    g = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    airPlane = deque([])
    
    for _ in range(n):
        temp = int(sys.stdin.readline())
        airPlane.append(temp)

    parent = [i for i in range(g+1)]

    res = solution()

    print(res)