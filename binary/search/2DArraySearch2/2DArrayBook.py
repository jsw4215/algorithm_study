def solution(matrix, target):

    if not matrix:
        return False

    row = 0
    col = len(matrix[0]) -1

    while row <= len(matrix) -1 and col >=0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col-=1
        elif target > matrix[row][col]:
            row+=1


    return False

if __name__ == '__main__':

    target = 20

    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

    result = solution(matrix, target)

    print(f'{result}')
