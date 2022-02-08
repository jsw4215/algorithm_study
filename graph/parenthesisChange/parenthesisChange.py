def correct_check(p):

    correct = True
    stack = []
    left = 0
    right = 0

    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
            left+=1
        else:
            right+=1
            if len(stack) == 0:
                correct = False
            else:
                stack.pop()

        if left==right:
            return correct, i+1

    return False, 0


def solution(p):
    if len(p)==0:
        return p

    correct, idx = correct_check(p)

    u = p[:idx]
    v = p[idx:]

    if correct:
        return u + solution(v)

    temp = '(' + solution(v) + ')'

    for i in range(1,len(u)-1):
        if u[i]=='(':
            temp+=')'
        else:
            temp+='('

    return temp


if __name__ == '__main__':

    p = "()))((()"

    result = solution(p)

    print('result : ' + str(result))