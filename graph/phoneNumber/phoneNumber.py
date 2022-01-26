def solution(inputNum):

    dic = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqr",
        "8":"stv",
        "9":"wxyz"
    }

    result = []

    def recursive_num(index, alpha):

        if len(alpha) == len(inputNum):
            result.append(alpha)
            return

        for i in range(index, len(inputNum)):
            for j in dic[inputNum[i]]:
                recursive_num(i+1, alpha + j)


    recursive_num(0,"")

    return result


if __name__ == '__main__':

    inputNum = '23'

    result = solution(inputNum)

    print('result : ' + str(result))