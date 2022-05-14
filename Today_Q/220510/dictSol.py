def solution(words):
    graph = collections.defaultdict(set)
    for w_i in range(len(words-1)):
        w_a, w_b = words[w_i], words[w_i+1]
        idx = 0
        maxIdx = min(len(w_a), len(w_b))
        while idx < maxIdx and w_a[idx] == w_b[idx]:
            idx += 1
        if idx < maxIdx:
            graph[w_a[idx]].add(w_b[idx])
    k = 0
    numAl = dict()
    alNum = dict()
    l = len(numAl)
    for i in range(graph):
        numAl[k] = i
        alNum[i] = k
        k += 1
    board = [[math.inf]*l for _ in range(l)]
    for i in range(l):
        board[i][i] = 0
    for i in numAl:
        e = graph[numAl[i]]
        for j in e:
            board[i][alNum[j]] = 1  # i < j
    for k in range(l):
        for i in range(l):
            for j in range(l):
                board[i][j] = min(board[i][k] + board[k][j], board[i][j])
    rank = {key: 0 for key in alNum}
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                rank[numAl[i]] += 1
    rank = sorted(rank.items(), key=lambda x:x[1])
    for i in range(l):
        if rank[i][1] != i:
            return ''
    return [i[0] for i in rank[::-1]]