from collections import deque
import copy
#cycle(빼는애, 넣는애)
def q1ToQ2(popQ, insertQ, time):
    popQCopy = copy.deepcopy(popQ)
    insertQCopy = copy.deepcopy(insertQ)

    temp = popQCopy.popleft()
    insertQCopy.append(temp)

    time+=1

    return [popQCopy, insertQCopy, time]

def q2ToQ1(popQ, insertQ, time):
    popQCopy = copy.deepcopy(popQ)
    insertQCopy = copy.deepcopy(insertQ)

    temp = popQCopy.popleft()
    insertQCopy.append(temp)

    time+=1

    return [insertQCopy, popQCopy, time]

def check(q1, q2):
    if sum(q1) == sum(q2):
        return True
    return False

def matcher(nowQ, q):
    for i in range(len(q)):
        if nowQ[i]!=q[i]:
            return False
    return True

def solution(q1, q2):

    if (sum(q1)+sum(q2))%2:
        return -1

    q1 = deque(q1)
    q2 = deque(q2)

    #q1이더 긴지, q2가 더 긴지
    checker = min(len(q1),len(q2))
    longer = len(q1)<=len(q2)
    q = deque([[q1, q2, 0]])

    while q:

        temp = q.popleft()
        sum1 = sum(temp[0])
        sum2 = sum(temp[1])
    
        if check(temp[0],temp[1]):
            return temp[2]

        if temp[0] and sum1>sum2:
            C1 = q1ToQ2(temp[0], temp[1], temp[2])
            if longer and len(C1[0])==checker:
                if matcher(C1[0], q1):
                    continue
            if not longer and len(C1[1])==checker:
                if matcher(C1[1], q2):
                    continue
            q.append(C1)

        if temp[1] and sum2>sum1:
            C2 = q2ToQ1(temp[1],temp[0], temp[2])
            if longer and len(C2[0])==checker:
                if matcher(C2[0], q1):
                    continue
            if not longer and len(C2[1])==checker:
                if matcher(C2[1], q2):
                    continue
            q.append(C2)

    return -1

if __name__ == '__main__':

    q1 = [3, 2, 7, 2]
    q2 = [4, 6, 5, 1]

    res = solution(q1, q2)

    print(res)