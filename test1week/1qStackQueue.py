def solution(progresses, speeds):
    finish = []
    stack = []

    for i in range(len(progresses)):
        curr = progresses[i]
        day = 0
        while(curr < 100):
            day += 1
            curr = curr + speeds[i]
        finish.append(day)
    [7,3,9]
    temp=0
    for fin in finish:
        if fin>temp:
            temp = fin
            stack.append(1)
        else :
            stack[-1]+=1

    print('stack : ' + str(stack))

    return stack


if __name__ == '__main__':

    progresses = [93, 30, 55]
    speeds = [1, 30, 5]

    result = solution(progresses, speeds)

    print('result : ' + str(result))