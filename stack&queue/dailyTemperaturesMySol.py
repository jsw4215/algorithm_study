def solution(Temperatures):

    result = [0]*len(Temperatures)

    for i in range(0,len(Temperatures)-1):
        for j in range(i,len(Temperatures)):
            if Temperatures[i] < Temperatures[j]:
                result[i]=j-i
                break


    return result


if __name__ == '__main__':

    T = [73,74,75,71,69,72,76,73]

    result = solution(T)

    print('result : ' + str(result))