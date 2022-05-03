def sol(target):

    targetStr = str(target)
    
    minStr = minCut(targetStr)

    maxStr = maxCut(targetStr)

    print("res!", minStr, maxStr)

    res = int(maxStr)-int(minStr)

    print("res!!", res)

    return res

def maxCut(targetStr):
    leadingChar = targetStr[0]

    if leadingChar=="9":
        targetChar=""
        if(len(targetStr)>1):
            num = nextNine(targetStr, 1)
            if(num==-1): return targetStr
            targetChar = targetStr[num]

        return targetStr.replace(targetChar, "9")

    else:
        return targetStr.replace(leadingChar, "9")
    

def minCut(targetStr):
    leadingChar = targetStr[0]

    if leadingChar=="1":
        targetChar=""
        if(len(targetStr)>1):
            num = nextZero(targetStr, 1)
            if(num==-1): return targetStr
            targetChar = targetStr[num]

        return targetStr.replace(targetChar, "0")

    else:
        return targetStr.replace(leadingChar, "1")
    
def nextZero(stringBef, i):
    if(i>=len(stringBef)):
        return -1

    if(stringBef[i]!="0") and (stringBef[i]!="1"):
        return i
    else:
        return nextZero(stringBef, i+1)

def nextNine(stringBef, i):
    if(i>=len(stringBef)):
        return -1

    if(stringBef[i]!="9"):
        return i
    else:
        return nextNine(stringBef, i+1)


if __name__ == '__main__':

    n = "112233445"

    palinList = sol(n)