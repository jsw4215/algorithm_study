from algorithm.stack_queue.structures import Stack


def solution(inputList):

    stack = []
    count = 0
    checker = True
    result = []

    for i in range(num):

        while inputList[i]>count:
            count += 1
            stack.append(count)
            result.append("+")

        print('stack : ' + str(stack) + ', inputList : ' + str(inputList))

        if stack[-1]==inputList[i]:
            stack.pop()
            result.append("-")
        else :
            checker = False
            break

    if checker == False:
        print("NO")
    else:
        print("\n".join(result))

    pass


if __name__ == '__main__':

    num = int(input())
    inputList = []

    for i in range(num):
        inputList.append(int(input()))

    result = solution(inputList)
