from collections import deque

from binary.prac import make_tree_by



def solution(root) -> int:
    longest = 0
    root = make_tree_by(binTree, 0)

    def dfs(node, level):
        if not node:
            return -1
        left = dfs(node.left, level+1)
        right= dfs(node.right, level+1)
        nonlocal longest
        longest = max(longest, left + right + 2)
        return max(left, right) + 1
    dfs(root,0)

    return longest

if __name__ == '__main__':

    binTree = [1,2,3,4,5]

    result = solution(binTree)

    print('result : ' + str(result))