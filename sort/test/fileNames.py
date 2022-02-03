def solution(files):

    #이분탐색으로 head와 num을 구분한다. - 불가
    #divide and conquer - 이유없음
    #str.index() 함수 사용 - 범위적용 안됨
    #그냥 for문

    result = []
    for file in files:
        headIdx = 0
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):

            if not headIdx and file[i].isdigit():
                head = file[:i]
                headIdx = i

            if headIdx and not file[i].isdigit():
                number = file[headIdx:i]
                tail = file[i:]
                result.append([head, number, tail])
                break

            if headIdx and i==len(file)-1 and number=='':
                number = file[headIdx:]
                result.append([head, number])


    print(f'{result}')

    result = sorted(result, key = lambda x:(x[0].lower(), int(x[1])))

    print(f'{result}')

    return [''.join(file) for file in result]

if __name__ == '__main__':

    #files = ["img12.png", "img10.png", "IMG02.png", "img1.png", "img01.GIF", "img2.JPG"]
    test = ["a9","e10","a0011","b012","u13","w014"]

    result = solution(test)

    print(f'{result}')
