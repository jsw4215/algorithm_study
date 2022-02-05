def solution(balls):
    result = []

    for i in range(len(balls)):
        for j in range(i, len(balls)):
            if balls[i] is not balls[j]:
                result.append([i+1,j+1])

    print(f'{result}')


if __name__ == '__main__':

    n, m = 5, 3
    balls = [1, 3, 2, 3, 2]

    solution(balls)

    # print(f'{l}')