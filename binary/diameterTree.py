from collections import deque

from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    leftDist = 0
    rightDist = 0

    def dfs_left_tree(level, node):
        if node is None:
            return -1

        if node.left:
            nonlocal leftDist
            leftDist = max(leftDist, level+1)
            dfs_left_tree(level+1, node.left)
        if node.right:
            nonlocal rightDist
            rightDist = max(rightDist, level + 1)
            dfs_left_tree(level + 1, node.right)

        leftDist = max(rightDist,leftDist)

        return leftDist


    finLeftDist = dfs_left_tree(0, root.left)
    leftDist = 0
    rightDist = 0
    finRightDist = dfs_left_tree(0, root.right)

    result = finLeftDist + finRightDist +2

    return result

if __name__ == '__main__':

    binTree = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]

    result = solution(binTree)

    print('result : ' + str(result))