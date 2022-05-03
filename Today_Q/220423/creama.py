def longest_palindrome(target):

    res = another(n)

    print("res!",res)

    return res

def another(n):
    if len(n)<3:
        if n=="":
            return -1
        else:
            return n
    else:
        temp = n.replace("AWS","")
        if len(temp) == len(n):
            return n
        else:        
            return another(temp)

def removeAWS(n):
    if len(n)<3:
        if n=="":
            return -1
        else:
            return n
        
    for i in range(len(n)-2):
        if n[i]=="A":
            if n[i+1]=="W":
                if n[i+2]=="S":
                    beforeStr = n[0:i]
                    afterStr = n[i+3:]
                    temp = beforeStr + afterStr
                    print("str cut", temp)
                    return removeAWS(temp)
    return n
    


if __name__ == '__main__':

    n = "AAWSWS"

    palinList = longest_palindrome(n)