def solution(n):


    for i in range(n):
        a=2*i+1
        print(" "*(n-i) + "*"*a)

    return

if __name__ == '__main__':

    n = 5

    solution(n)