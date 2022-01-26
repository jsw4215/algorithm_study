#binary DFS Templates
from collections import deque

from binary.prac import make_tree_by
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(rawNodes):

    nodes = rawNodes[:]

    root = TreeNode(nodes.pop(0)[0])

    def dfs_make(root, level):

        for node in nodes:

            if root.left is None and root.val in node:
                node.remove(root.val)
                root.left = TreeNode(node[0])
                nodes.remove(node)
                dfs_make(root.left, level + 1)
            if root.right is None and root.val in node:
                node.remove(root.val)
                root.right = TreeNode(node[0])
                nodes.remove(node)
                dfs_make(root.right, level + 1)


    dfs_make(root, 0)

    print(f'{root}')

    pass

if __name__ == '__main__':

    n = 7
    rawNodes = [['1'], ['1', '6'], ['6', '3'], ['3', '5'], ['4', '1'], ['2', '4'], ['4', '7']]

    # for i in range(n-1):
    #     nodes.append(input().split())

    print(f'{rawNodes}')

    result = solution(rawNodes)

    print('result : ' + str(result))