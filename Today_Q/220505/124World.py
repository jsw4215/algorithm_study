def solution(n):
    nara = [1,2,4]
    answer = ''
    
    while True:
        if n <= 0:
            return answer
        n -= 1
        answer = str(nara[n%3]) + answer
        n //= 3


if __name__ == '__main__':

    n = int(input())
    
    solution(n)

    