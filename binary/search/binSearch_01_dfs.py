#binary DFS Templates
from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    dist = []

    def dfs(node, level):
        if node is None:
            return None

        #
        # 로직 구현
        #

        if node.left:
            node.left = dfs(node.left, level+1)
        if node.right:
            node.right = dfs(node.right, level+1)

        return node

    dfs(root, 0)


    pass

if __name__ == '__main__':

    binTree = [1,2,3,None,None,4,5]

    result = solution(binTree)

    print('result : ' + str(result))