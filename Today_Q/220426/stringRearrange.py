def solution(data):

    resStr = ""
    resInt = 0

    for i in range(len(data)):
        if data[i].isalpha():
            resStr+=data[i]
        else:
            resInt+=int(data[i])
    
    resStr = ''.join(sorted(resStr))

    print(resStr+str(resInt))

    pass


if __name__ == '__main__':

    data = input()
    solution(data)