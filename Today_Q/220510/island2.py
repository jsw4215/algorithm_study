dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
bitmap=[[]]
r, c = len(bitmap), len(bitmap[0])
ans = []
for i in range(r):
    for j in range(c):
        if bitmap[i][j]:
            area = 1
            stack = [(i, j)]
            bitmap[x][y] = 0
            while stack:
                x, y = stack.pop()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0<=nx<r and 0<=ny<c and bitmap[nx][ny]:
                        stack.append((nx, ny))
                        bitmap[nx][ny] = 0
                        area+=1
            ans.append(area)