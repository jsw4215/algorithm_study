def solution(dummy):

    for i in range(len(dummy)-1, 0 , -1):
        for j in range(i):
            if dummy[j][0] > dummy[j+1][0]:
                dummy[j], dummy[j+1] = dummy[j+1], dummy[j]
            elif dummy[j][0] == dummy[j+1][0]:
                if dummy[j][1] > dummy[j+1][1]:
                    dummy[j], dummy[j+1] = dummy[j+1], dummy[j]

    print(f'{dummy}')

    pass


if __name__ == '__main__':

    n = 5
    dummy = [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]

    solution(dummy)

    # print(f'{l}')