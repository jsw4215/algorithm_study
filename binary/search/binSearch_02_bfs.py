#binary DFS Templates
from collections import deque

from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    queue = deque([root])

    result = []

    def serialize(queue):
        while queue:
            node = queue.popleft()

            if node:
                #
                #로직 구현
                #
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('#')
        return result

    result=serialize(queue)

    print(f'{result}')

    def deserialize(serializedStr):
        nodes = serializedStr

        print(f'{nodes}')



    deserialize(result)

    return root

if __name__ == '__main__':

    binTree = [1,2,3,None,None,4,5]

    result = solution(binTree)

    print('result : ' + str(result))