def solution(matrix, target):

    checker = False


    def bin_search():

        left = 0
        right = len(matrix)-1

        while left <=right:

            mid = (left + right) // 2

            if target > matrix[mid][0]:
                left = mid+1
            elif target < matrix[mid][0]:
                right = mid-1
            else:
                return mid + 1

        mid = max(left,right)
        return mid


    lineRIdx = bin_search()


    def bin_search2(lineLimit):

        temp_matrix = matrix[:lineLimit]
        i=0

        for i in range(lineLimit):

            left = 0
            right = len(temp_matrix[i])-1

            while left <= right:

                mid = (left + right) // 2

                if target > matrix[i][mid]:
                    left = mid + 1
                elif target < matrix[i][mid]:
                    right = mid - 1
                else:
                    return True

            i += 1
        return False


    checker = bin_search2(lineRIdx)

    return checker

if __name__ == '__main__':

    target = 20

    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

    result = solution(matrix, target)

    print(f'{result}')
