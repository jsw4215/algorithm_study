def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret