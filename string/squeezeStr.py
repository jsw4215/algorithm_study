def squeeze(strs):
    data = []
    result = ""
    answer = 1000
    # len(strs)//2 + 2
    for i in range(1, len(strs) // 2 + 2):

        temp = strs[:i]
        count = 1
        for j in range(i, len(strs)+i, i):
            temp2 = strs[j:j+i]
            if temp == temp2:
                count += 1
            else:
                if count == 1:
                    result += temp
                    temp = temp2
                else:
                    result += str(count)+temp
                    temp = temp2
                    count=1
        data.append(result)
        result=""

    fin = []

    for i in data:
        fin.append(len(i))



    print(f'{data}')

    return min(fin)


if __name__ == '__main__':

    n = "ababcdcdababcdcd"

    result = squeeze(n)
    print(f'result: {result}')
