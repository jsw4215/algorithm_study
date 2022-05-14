def solution(boxes):
    # 왼쪽 아래 x, y, 오른쪽 위 x, y 4개가 주어진다.
    def included(one, another, p):
        le, lo, ri, hi = one
        le_, lo_, ri_, hi_ = another
        # le, lo가 포함되는 경우
        if le_ < le < ri_ and lo_ < lo < hi_:
            return True
        # le, hi가 포함되는 경우
        if le_ < le < ri_ and lo_ < hi < hi_:
            return True
        # ri, lo가 포함되는 경우
        if le_ < ri < ri_ and lo_ < lo < hi_:
            return True
        # ri, hi가 포함되는 경우
        if le_ < ri < ri_ and lo_ < hi < hi_:
            return True
        if p:
            return False
        return included(another, one, 1)

    def check(box):
        for another in already:
            if included(box, another, 0):
                return False
        return True

    ans = []
    already = []
    for idx in range(len(boxes)):
        box = boxes[idx]
        if check(box):
            ans.append(idx)
            already.append(box)
    return ans