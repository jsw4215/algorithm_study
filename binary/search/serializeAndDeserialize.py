#binary DFS Templates
from collections import deque

from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:

            #로직 구현



            queue.append(node.left)
            queue.append(node.right)

    return root

if __name__ == '__main__':

    binTree = [4,2,7,1,3,6,9]

    result = solution(binTree)

    print('result : ' + str(result))