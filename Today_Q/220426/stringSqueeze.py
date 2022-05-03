def solution(data):

    res = 1000
    result = ""

    for i in range(1,len(data)//2):
        
        temp = data[:i]
        count = 1

        for j in range(i, len(data)//2+i, i):
            temp2 = data[j:j+i]
            if temp == temp2:
                count+=1
            else:
                if count==1:
                    result+=temp
                else:
                    result+=(str(count)+temp)

    print("res", result)

    pass


if __name__ == '__main__':

    data = "abcabcabcabcdededededede"

    solution(data)