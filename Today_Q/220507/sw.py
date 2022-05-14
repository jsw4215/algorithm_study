import math

def ansCheck(l, r, len1, len2, W, ans):
    if 0 < l and r < len1:
        return min(r + len2, ans)
    elif 0 < l and len1 < r < W:
        return min(r-len1, ans)
    elif 0 < l < len1 and r < len1:
        return min(W+l, ans)
    elif 0 < l < len1 and r == len1:
        return min(l, ans)
    elif 0 < l < len1 and len1 < r < W:
        return min(r+l-len1, ans)
    elif 0 < l < len1 and r == W:
        return min(l, ans)
    elif l == len1 and len1 < r < W:
        return min(r-l, ans)
    elif len1 < l and len1 < r < W:
        return min(r+l-len1, ans)
    elif len1 < l and r == W:
        return min(l, ans)
    return ans

def checker(q1, q2):
    if sum(q1) == sum(q2):
        return True
    return False

def solution(q1, q2):
    tot = sum(q1)+sum(q2)
    if (tot)%2:
        return -1

    check = tot//2

    if checker(q1,q2):
        return 0
    arr = q1 + q2
    len1 = len(q1)
    len2 = len(q2)
    W = len(arr)
    ans = math.inf

    temp = arr[0]
    l=0
    r=1

    while r < W and l < r:
        
        if check == temp:
            ans = ansCheck(l, r, len1, len2, W, ans)

        if temp < check:
            temp+=arr[r]
            r+=1
        else:
            temp+=arr[l]
            l+=1

    if ans == math.inf:
        return -1
    else:
        return ans

if __name__ == '__main__':

    q1 = [3, 2, 7, 2]
    q2 = [4, 6, 5, 1]

    res = solution(q1, q2)

    print(res)