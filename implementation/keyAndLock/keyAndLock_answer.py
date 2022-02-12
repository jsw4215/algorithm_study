#실패코드
from collections import deque


def solution(keys, lock):

    key_rows = len(keys)
    key_cols = len(keys[0])

    lock_rows = len(lock)
    lock_cols = len(lock[0])

    new_lock = [[0 for _ in range(lock_rows*3)] for _ in range(lock_cols*3)]


    #자물쇠를 가운데 삽입
    for i in range(lock_rows):
        for j in range(lock_cols):
            new_lock[lock_rows+i][lock_cols+j] = lock[i][j]

    def rotate_90(m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N - 1 - r] = m[r][c]
        return ret

    def check(new_lock):
        n = len(new_lock) // 3

        for i in range(n, n * 2):
            for j in range(n, n * 2):
                if new_lock[i][j] != 1:
                    return False

        return True


    rotatedKey = keys

    for x in range(lock_rows*2):
        for y in range(lock_cols*2):
            for _ in range(4):
                rotatedKey = rotate_90(rotatedKey)
                for key_x in range(key_rows):
                    for key_y in range(key_cols):
                        new_lock[x+key_x][y+key_y] += rotatedKey[key_x][key_y]

                if check(new_lock):
                    return True

                for key_x in range(key_rows):
                    for key_y in range(key_cols):
                        new_lock[x+key_x][y+key_y] -= rotatedKey[key_x][key_y]


    return False






if __name__ == '__main__':

    key = [
        [0,0,0],
        [1,0,0],
        [0,1,1]
    ]
    lock = [[1,1,1],[1,1,0],[1,0,1]]

    result=solution(key, lock)

    print(f'{result}')