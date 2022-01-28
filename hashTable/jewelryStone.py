def solution(jewel, stone):

    hash = {}

    for s in stone:
        if s not in hash:
            hash[s] = 1
        else:
            hash[s] += 1

    count=0

    for j in jewel:
        if j in hash:
            count+=hash[j]

    return count


if __name__ == '__main__':

    J = 'z'
    S = 'ZZ'

    result = solution(J,S)

    print('result : ' + str(result))