import sys


def solution(dirs):
    command = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    road = set()
    cur_x, cur_y = (0, 0)

    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2

if __name__ == '__main__':

    n = input()

    result = solution(n)

    print('result : ' + str(result))
