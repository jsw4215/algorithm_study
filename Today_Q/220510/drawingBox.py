def boxChecker(box, nextBox, checker):
    res = False

    

    #X1이 동일한 경우
    if box[0]==nextBox[0] and box[1]<nextBox[3]<=box[3]:
        return True
    #X1이 동일한 경우
    if box[0]==nextBox[0] and box[1]<=nextBox[1]<box[3]:
        return True
    
    #X2가 동일한 경우
    if box[2]==nextBox[2] and box[1]<=nextBox[1]<box[3]:
        return True
    #X2가 동일한 경우
    if box[2]==nextBox[2] and box[1]<nextBox[3]<=box[3]:
        return True


    #Y1이 동일한 경우
    if box[1]==nextBox[1] and box[0]<=nextBox[0]<box[2]:
        return True
    if box[1]==nextBox[1] and box[0]<nextBox[2]<=box[2]:
        return True


    #Y2가 동일한 경우
    if box[3]==nextBox[3] and box[0]<=nextBox[0]<box[2]:
        return True
    if box[3]==nextBox[3] and box[0]<nextBox[2]<=box[2]:
        return True

    #변 위에 점이 있는 경우

    #겹침 체크
    #1. 좌측하단이 범위내에 있을 경우
    if box[0]<nextBox[0]<box[2] and box[1]<nextBox[1]<box[3]:
        return True
    #2. 좌측상단이 범위내에 있을 경우
    if box[0]<nextBox[0]<box[2] and box[1]<nextBox[3]<box[3]:
        return True
    #3. 우측하단이 범위내에 있을 경우
    if box[0]<nextBox[2]<box[2] and box[1]<nextBox[1]<box[3]:
        return True
    #4. 우측상단이 범위내에 있을 경우
    if box[0]<nextBox[2]<box[2] and box[1]<nextBox[3]<box[3]:
        return True

    if checker:
        checker = False
        res = boxChecker(nextBox, box, checker)

    return res


def solution(boxList):

    if len(boxList)==0:
        return []

    ans = [0]
    validBox = [boxList[0]]

    for i in range(1, len(boxList)):
        checker = True
        for box in validBox:
            if boxChecker(box, boxList[i], True):
                checker = False
        if checker:
            ans.append(i)
            validBox.append(boxList[i])

    return ans

if __name__ == '__main__':

    grid = [
        [1,1,3,3],
        [2,2,4,4],
        [1,2,4,4],
        [3,3,5,5]
    ]

    result = solution(grid)

    print('result : ' + str(result))