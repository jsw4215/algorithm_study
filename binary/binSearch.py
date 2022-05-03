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

        return max(left,right)

    dfs(root, 0)

    pass

if __name__ == '__main__':

    binTree = [5,4,5,1,1,None,5]

    result = solution(binTree)

    print('result : ' + str(result))