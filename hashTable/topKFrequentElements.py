def solution(elements, k):

    hash = {}
    result = []

    for e in elements:
        if e in hash:
            hash[e]+=1
        else:
            hash[e]=1

    for i in hash:
        if hash[i]>=k:
            result.append(i)

    return result


if __name__ == '__main__':

    nums = [1,1,1,2,2,3]
    k = 2

    result = solution(nums, k)

    print('result : ' + str(result))