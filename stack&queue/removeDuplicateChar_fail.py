import collections
import re

def solution(inputStr):
    originStr = inputStr
    counter, seen, stack = collections.Counter(inputStr), set(), []
    stringSet = sorted(set(inputStr))
    print('counter : ' + str(counter) + ', seen : ' + str(seen) + ', stack : ' + str(stack))

    print('sorted(set(inputStr)) : ' + str(stringSet))

    result= {}

    for i in range(len(stringSet)):
        char = stringSet[i]
        #같은 문자 몇번째인지 체크
        checker = 0
        while counter[char]:
            counter[char] -= 1
            # 문자열(문자를 삭제할) 내 문자의 위치 찾기
            idxInInputForDel = inputStr.find(char)
            # 입력값 문자열(원본) 내 문자의 위치 찾기
            checker+=1
            dup_ck = checker
            #문자가 여러개일 경우 몇번째 문자인지 찾기
            for m in re.finditer(f'{char}', originStr):
                idxInInput = m.start()
                dup_ck-=1
                if dup_ck<=0:
                    break

            #뒤에 해당 char문자가 더 있다면,
            if counter[char]!=0 :
                #해당 문자보다 앞선(문자열 내 서열) 문자들이, 뒤에 있는지 비교하기
                for j in range(i):
                    prevChar = stringSet[j]
                    #char보다 앞선 문자가 뒤에 있으면, 결과 값에 넣지 않고, 뒤에서 넣어야 하니 삭제, 단 조건이 하나 더 있다.
                    if prevChar in originStr[idxInInput+1:]:
                        #같은 문자의 다음 위치가, 뒤에 있는 1개남은 서열 낮은 문자보다 뒤에 있으면 지우면 안된다.
                        tempStr = originStr[idxInInput+1:]
                        sameCharNextIdx = tempStr.find(char)
                        for k in range(i+1,len(stringSet)):
                            nextChar = stringSet[k]
                            if counter[nextChar]==1:
                                nextCharIdx = tempStr.find(nextChar)
                                if sameCharNextIdx>nextCharIdx and nextCharIdx!=-1:
                                    #살리는 대신, 나머지 죽이기
                                    break
                                else:
                                    inputStr = inputStr[:idxInInputForDel] + inputStr[idxInInputForDel + 1:]
                                    break

    return inputStr



if __name__ == '__main__':

    input = 'cbacdcbc'

    result = solution(input)

    print('result : ' + str(result))