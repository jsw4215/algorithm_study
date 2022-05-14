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

def validLoop(box, validBoxes):
    for validBox in validBoxes:
        if boxChecker(box, validBox, True):
            return False
    return True

def solution(boxList):

    ans = []
    validBox = []

    for i in range(len(boxList)):
        box = boxList[i]

        if box[0]==box[2] and box[1]==box[3]:
            continue

        if validLoop(box, validBox):
            ans.append(i)
            validBox.append(box)

    return ans