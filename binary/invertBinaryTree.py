from collections import deque

from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    dist = []

    def dfs(node, level):
        if node is None:
            return 0

        # leftTemp = node.left
        # rightTemp = node.right
        #
        # node.right = leftTemp
        # node.left = rightTemp
        
        node.left, node.right = node.right, node.left

        left = dfs(node.left, level+1)
        right = dfs(node.right, level+1)

        return max(left,right)

    dfs(root, 0)


    pass

if __name__ == '__main__':

    binTree = [4,2,7,1,3,6,9]

    result = solution(binTree)

    print('result : ' + str(result))