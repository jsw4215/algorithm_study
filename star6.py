def solution(inputNum):



    for i in range(inputNum+1):
        star = inputNum*2-2*i-1
        print(" "*i+"*"*star)



    pass


if __name__ == '__main__':

    inputNum = 5

    result = solution(inputNum)