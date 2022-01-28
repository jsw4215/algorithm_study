def right_place(now_line, vstd):

    #같은 열

    for i in range(now_line):
        if vstd[i] == vstd[now_line] or now_line - i == abs(vstd[now_line] - vstd[i]):
            return False

    #대각선

    # for i in range(now_line):
    #     if now_line - i == abs(vstd[now_line] - vstd[i]):
    #         return False

    return True


def solution(n):
    count = 0
    result = []
    visited = [-1]*n

    #경우의 수 별로 Q 놓기
    def setQueens(line):

        #line이 n을 넘어갔다는건, all True가 나왔다는 것
        #all True시, 해당 count와 행렬을 출력해주기

        if line>=n :
            nonlocal count
            count+=1

            board = [["."]*n for _ in range(n)]

            print(f'{count}번째')

            for i, position in enumerate(visited):
                board[i][position]="Q"
                print(f'{board[i]}')

            return


        for i in range(n):
            #board[0][i]="Q"
            #print(f'{board}')

            #첫 줄의 i번에째 Q를 놓아본다.
            visited[line] = i
            if right_place(line, visited):
                setQueens(line+1)


    setQueens(0)




    # def dfs_stack(start):
    #
    #     visited = []
    #     stack = [start]
    #
    #     top = stack.pop()
    #     visited.append(top)
    #
    #     while stack:
    #         for adj in board[top]:
    #             if adj not in visited:
    #                 stack.append(adj)
    #
    #     return visited

    pass


if __name__ == '__main__':

    n = 4

    result = solution(n)
