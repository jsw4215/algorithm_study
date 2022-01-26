def solution(strs):
    result = {}

    for i in range(len(strs)):
        result[1] = strs[i]
        for j in range(i+1,len(strs)):
            temp= strs[i:j]
            if strs[j] not in temp:
                if j-i+1 not in result:
                    result[j-i+1] = strs[i:j+1]
            else:
                break

    ansKey=max(result.keys())
    ret=result[ansKey]

    return ansKey


if __name__ == '__main__':

    strs = 'abcabcbb'

    result = solution(strs)

    print('result : ' + str(result))