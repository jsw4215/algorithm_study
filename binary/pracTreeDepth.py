from collections import deque

from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    q = deque([root])
    depth = 0

    while q:
        depth+=1
        for _ in range(len(q)):
            temp = q.popleft()
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    return depth

if __name__ == '__main__':

    binTree = [3,9,20,None,None,15,7]

    result = solution(binTree)

    print('result : ' + str(result))