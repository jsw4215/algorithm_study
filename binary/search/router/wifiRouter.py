def solution(n, m, l1):

    l1.sort()

    left = 1
    right = l1[-1] - l1[0]
    result = -1


    while left <= right :
        dist = []
        distance = (right + left) // 2
        routerInstalled = l1[0]
        count=1

        for i in range(1,len(l1)):
            if routerInstalled + distance <= l1[i]:
                dist.append(l1[i] - routerInstalled)
                routerInstalled = l1[i]
                count+=1

        if count >= m :
            left = distance+1
            if result == -1:
                result = min(dist)
            elif result < min(dist):
                result = min(dist)
        else:
            right = distance-1



    return result


if __name__ == '__main__':

    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    l1 = []

    for i in range(n):
        temp=int(input())
        l1.append(temp)

    result = solution(n, m, l1)

    print(str(result))