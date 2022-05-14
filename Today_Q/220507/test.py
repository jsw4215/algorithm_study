def rotate_90(table, H, W, N):  
    temp = table[0][0]
    # left
    for i in range(1, H):
        table[i-1][0] = table[i][0]
    # bottom
    for i in range(1, W):
        table[H-1][i-1] = table[H-1][i]
    # right
    for i in range(H-2, -1, -1):
        table[i+1][W-1] = table[i][W-1]
    # top
    for i in range(W-2, 0, -1):
        table[0][i+1] = table[0][i]
    table[0][1] = temp
    
    return deque(table)