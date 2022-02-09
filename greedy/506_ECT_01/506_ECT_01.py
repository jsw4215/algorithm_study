def solution(n, lst):

    lst.sort(reverse=True)

    temp=0
    cnt = 0
    while temp<=n:
        temp+=lst.pop(0)
        cnt+=1

    if temp>n:
        cnt-=1

    print(f'{cnt}')


if __name__ == '__main__':

    n =  5
    lst = [2,3,1,2,2]

    solution(n, lst)

    # print(f'{l}')