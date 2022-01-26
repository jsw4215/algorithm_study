#binary DFS Templates
from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    dist = []

    def dfs(node, level):
        if node is None:
            return 0

        left = dfs(node.left, level+1)
        right = dfs(node.right, level+1)

        #
        # 로직 구현
        #
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left,right) + 1

    result = dfs(root, 0)


    return result != -1

if __name__ == '__main__':

    binTree = [1,2,2,3,3,None,None,4,4]

    result = solution(binTree)

    print('result : ' + str(result))