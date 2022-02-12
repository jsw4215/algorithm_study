#실패코드
from collections import deque


def solution(keys, lock):

    key_rows = len(keys)
    key_cols = len(keys[0])

    lock_rows = len(lock)
    lock_cols = len(lock[0])

    #shift up/down/left/right
    def shift_R(key):
        key = deque(key)
        for _ in range(len(key)):
            row = key.popleft()
            de_row = deque(row)
            de_row.pop()
            de_row.appendleft(0)
            key.append(de_row)
        return key


    def shift_L(key):
        key = deque(key)
        for _ in range(len(key)):
            row = key.popleft()
            de_row = deque(row)
            de_row.popleft()
            de_row.appendleft(0)
            key.append(de_row)
        return key

    def shift_Up(key):
        key = deque(key)
        key.popleft()
        key.append([0] * key_rows)
        return key

    def shift_Down(key):
        key = deque(key)
        key.pop()
        key.appendleft([0] * key_rows)
        return key

    def rotate_90(m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N - 1 - r] = m[r][c]
        return ret


    def matcher(key):

        if lock_cols > key_cols:

            diff = lock_cols - key_cols
            for diff_x in range(diff):
                for diff_y in range(diff):
                    for x in range(key_rows):
                        for y in range(key_cols):
                            if key[x+diff_x][y+diff_y] + lock[x][y] != 1:
                                return False

        elif lock_cols < key_cols:

            diff = key_cols - lock_cols
            for diff_x in range(diff):
                for diff_y in range(diff):
                    for x in range(lock_rows):
                        for y in range(lock_cols):
                            if key[x][y] + lock[x+diff_x][y+diff_y] != 1:
                                return False

        else:

            for x in range(key_rows):
                for y in range(key_cols):
                    if key[x][y] + lock[x][y] != 1:
                        return False

        return True

    rotatedKey = []
    RUkey = []
    Rkey = []
    RDkey = []
    Lkey = []
    LUkey = []
    LDkey = []
    answer = False

    rotatedKey = keys
    for _ in range(4):
        #90/180/270/360도 돌린다
        rotatedKey = rotate_90(rotatedKey)
        answer = matcher(rotatedKey)
        if answer:
            return True
        Rkey = rotatedKey
        Lkey = rotatedKey
        #우 + up, 우 + down // 좌 + up, 좌 + down
        for _ in range(key_rows):
            Rkey = shift_R(Rkey)
            answer = matcher(Rkey)
            if answer:
                return True
            RUkey = Rkey
            RDkey = Rkey
            for _ in range(key_cols):
                RUkey = shift_Up(RUkey)
                answer = matcher(RUkey)
                if answer:
                    return True
                RDkey = shift_Down(RDkey)
                answer = matcher(RDkey)
                if answer:
                    return True

            Lkey = shift_L(Lkey)
            answer = matcher(Lkey)
            if answer:
                return True
            LUkey = Lkey
            LDkey = Lkey
            for _ in range(key_cols):
                LUkey = shift_Up(LUkey)
                answer = matcher(LUkey)
                if answer:
                    return True
                LDkey = shift_Down(LDkey)
                answer = matcher(LDkey)
                if answer:
                    return True

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