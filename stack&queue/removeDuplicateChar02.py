import collections
import re

def solution(inputStr):
    counter = collections.Counter(inputStr)
    stringSet = sorted(set(inputStr))
    print('counter : ' + str(counter))

    print('sorted(set(inputStr)) : ' + str(stringSet))

    result=[]

    result.append(inputStr)

    for char in stringSet:
        result=charOnePreserver(result,char)

    print('result : ' + str(result))
    result.sort()
    print('sorted result : ' + str(result))
    res = result[0]

    return res

def charOnePreserver(input, char):
    result = []
    inputStrList = []
    # 반복시마다 문자열을 초기값으로 돌려놓음
    inputStrList.append(input)
    print('==========================CHAR : ' + char)

    for _str in input:

        idxInInput = []

        for m in re.finditer(f'{char}', _str):
            idxInInput.append(m.start())

        # i 만 살리고 나머지 지우기 로직
        for i in range(len(idxInInput)):
            # 반복시마다 문자열을 초기값으로 돌려놓음
            inputStr = _str

            target = idxInInput[i]
            print(
                '---------------------idxList : ' + str(idxInInput) + ', i : ' + str(i) + ', preserve target : ' + str(
                    target))

            # 만약 inxInInput len이 1이면, break
            if len(idxInInput) == 1:
                result.append(inputStr)
                print('can not delete char : ' + char)
                break

            find_num = 0
            del_helper = 0
            # i 번째 문자만 살리고 나머지 삭제하기
            for m in re.finditer(f'{char}', inputStr):
                print('char!!!! : ' + char + ', inputStr : ' + inputStr + ', find_num : ' + str(
                    find_num) + ', i : ' + str(i))
                if find_num == i:
                    # 보존
                    print('preserve : ' + inputStr)
                else:
                    # 삭제
                    del_idx = m.start() - del_helper
                    print('del_idx : ' + str(del_idx))
                    print('before inputStr : ' + inputStr)
                    inputStr = inputStr[:del_idx] + inputStr[del_idx + 1:]
                    print('after inputStr : ' + inputStr)
                    del_helper += 1
                find_num += 1
            result.append(inputStr)
        print('++++++++++++++++++++result :' + str(result))

    return result

if __name__ == '__main__':

    input = 'ghadedfaih'

    result = solution(input)

    print('result : ' + result)