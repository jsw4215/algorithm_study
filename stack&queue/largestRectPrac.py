def solution():

    stack = []
    result = 0

    for idx, height in enumerate(heights):

        if stack == []:
            stack.append([idx, height])

        #stack에 있는 높이보다 더 낮은 높이가 나오면, stack을 pop하고, 각 높이에 대한 좌변 우변
        #(해당 높이보다 적은 값 나오기 전)을 구하여 너비를 구한다.
        else:
            #생각해내기 어려운 한줄
            leftSide = idx

            while stack != [] and height < stack[-1][1] :

                value = stack.pop()
                leftSide = value[0]
                stackHeight = value[1]
                #stack 안에 들어있는 데이터라는건, 우변은 현재 idx로 확정되었고, 내부에 stack이 더 있을 경우엔,
                # 좌변도 확정되어있다. 내부에 stack되어있는 데이터가 더 없을 경우가 있을 수가 있나? 생각을 해보자 머리가 안돌아간다.
                area = stackHeight*(idx - leftSide)

                if result < area:
                    result = area

            stack.append([leftSide, height])

    for remain in stack:
        challenger = remain[1]*(len(heights)-remain[0])
        if challenger > result:
            result = challenger

    return result


if __name__ == '__main__':

    heights = [2,1,5,6,2,3]

    result = solution()

    print(f'result: {result}')