def solution(n, m):

    cnt=0
    while n!=1:
        if n%m==0:
            n=n//m
            cnt+=1
        else:
            n-=1
            cnt+=1

    print(f'{cnt}')

if __name__ == '__main__':

    n, m = 25, 5

    solution(n, m)

    # print(f'{l}')