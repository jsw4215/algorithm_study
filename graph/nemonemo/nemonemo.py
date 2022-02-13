import sys


def dfs(cnt):
    global answer
    # 모든 칸을 확인한 경우 정답 1개 카운트
    if cnt == Y * X:
        answer += 1
        return

    # 현재 좌표
    y, x = cnt // X, cnt % X

    # 좌표가 범위내에 있는경우
    # 상, 좌, 상좌 위치에 네모가 있으면 바로 다음 칸확인
    if (0 < y < Y and 0 < x < X) and (arr[y - 1][x] and arr[y][x - 1] and arr[y - 1][x - 1]):
        dfs(cnt + 1)
    # 네모가 없는 경우
    else:
        # 네모 추가한 경우 확인
        arr[y][x] = 1
        dfs(cnt + 1)
        # 추가하지 않은 경우 확인
        arr[y][x] = 0
        dfs(cnt + 1)


Y, X = map(int, sys.stdin.readline().split())
arr = [[0] * X for _ in range(Y)]
answer = 0
dfs(0)
print(answer)