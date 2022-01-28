#binary DFS Templates
import sys

from binary.prac import make_tree_by


def solution(n, nodes, target):


    root = make_tree_by(nodes, 0)

    dist = []

    def dfsDelete(node, level):
        if node is None:
            return None

        if node.left and node.left.val == target:
            node.left = None
        if node.right and node.right.val == target:
            node.right = None
        else:
            node.left = dfsDelete(node.left, level+1)
            node.right = dfsDelete(node.right, level+1)

        #
        # 로직 구현
        #
        return node

    dfsDelete(root, 0)

    count = 0

    def dfs(node, level):
        if node is None:
            return None

        #
        # 로직 구현
        #

        node.left = dfs(node.left, level+1)
        node.right = dfs(node.right, level+1)

        if node.left is None and node.right is None:
            nonlocal count
            count+=1

        return node

    dfs(root, 0)

    return count

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    nodes = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    print(f'{nodes}')

    result = solution(n, nodes, target)

    print('result : ' + str(result))