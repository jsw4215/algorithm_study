def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    
    if total%2:
        return -1
    
    target = total//2

    if sum(queue1) == target:
        return 0
    
    l1, l2 = len(queue1), len(queue2)
    w = l1+l2
    case1 = queue1+queue2  # l1 + l2 꼴

    ret = float('inf')

    l, r, mid = 0, 1, case1[0]
    while r < w and l < r:
        if mid == target:
            if not l and r < l1:
                ret = min(ret, r+l2)
            elif not l and l1 < r < w:
                ret = min(ret, r-l1)
            elif 0 < l < l1 and r < l1:
                ret = min(ret, w+l)
            elif 0 < l < l1 and r == l1:
                ret = min(ret, l)
            elif 0 < l < l1 and l1 < r < w:
                ret = min(ret, r+l-l1)
            elif 0 < l < l1 and r == w:
                ret = min(ret, l)
            elif l == l1 and l1 < r < w:
                ret = min(ret, r-l)
            elif l1 < l and l1 < r < w:
                ret = min(ret, r+l-l1)
            elif l1 < l and r == w:
                ret = min(ret, l)
        if mid < target:
            mid += case1[r]
            r += 1
        else:
            mid -= case1[l]
            l += 1

    return -1 if ret == float('inf') else ret