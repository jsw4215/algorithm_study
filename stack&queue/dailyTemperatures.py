def dailyTemperatures(T):
    ret = [0] * len(T)
    stack = []

    for i, temp in enumerate(T):
        #순서대로 stack에 넣다가, 온도가 높을 때만 while문 돈다
        if i!=0:
            print('==================================== Day Temperature : ' + str(temp) + ', T[stack[-1]] : ' + str(T[stack[-1]]) + ', i : ' + str(i))
        else :
            print('==================================== Day Temperature : ' + str(temp) + ', i : ' + str(i))
        while stack and T[stack[-1]] < temp:
            #stack을 인덱스 리스트로 활용
            print('stack[-1] : ' + str(stack[-1]) + ', T[stack[-1]] : ' + str(T[stack[-1]]) + ', temp : ' + str(temp))
            print('before pop from stack : ' + str(stack))
            #맨 뒤의 값을 뽑는다
            index = stack.pop()
            print('after pop from stack : ' + str(stack))
            print('i - index : ' + str(i - index) + ', i : ' + str(i) + ', index : ' + str(index))
            ret[index] = i - index
            print('ret[] : ' + str(ret))
        #i를 넣어준다
        stack.append(i)
        print('------------------------ push stack : ' + str(stack))

    return ret


if __name__ == '__main__':

    T = list([73,74,75,71,69,72,76,73])


    result = dailyTemperatures(T)

    print('result : ' + str(result))