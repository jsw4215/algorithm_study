def solution(data):

    print(len(data))

    divider = len(data)//2
    answer = 0
    for i in range(len(data)):
        answer+=int(data[i]) if i<divider else -int(data[i])
    
    print('READY' if answer else 'LUCKY')

    pass 


if __name__ == '__main__':

    data = input()
    solution(data)