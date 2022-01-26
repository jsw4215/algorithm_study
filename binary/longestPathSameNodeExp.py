from binary.prac import make_tree_by


def solution(binaryTreeList):

    root = make_tree_by(binaryTreeList, 0)

    dist = []
    result=0

    def dfs(node, level):
        if node is None:
            return 0

        left = dfs(node.left, level+1)
        right = dfs(node.right, level+1)

        if node.left and node.left.val == node.val:
            left+=1
        else:
            left=0
        if node.right and node.right.val == node.val:
            right+=1
        else:
            right=0

        nonlocal result
        result = max(result, left + right)

        return max(left,right)

    dfs(root, 0)


    return result

if __name__ == '__main__':

    binTree = [5,4,5,1,1,None,5]

    result = solution(binTree)

    print('result : ' + str(result))