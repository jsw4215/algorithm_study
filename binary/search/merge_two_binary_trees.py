#binary DFS Templates
from binary.prac import make_tree_by
from binary.structures import TreeNode


def solution(binaryTreeList1, binaryTreeList2):

    root1 = make_tree_by(binaryTreeList1, 0)
    root2 = make_tree_by(binaryTreeList2, 0)
    result = TreeNode()
    dist = []

    def dfs(node1, node2, level):
        if node1 and node2:

            result = TreeNode(node1.val + node2.val)

            result.left = dfs(node1.left, node2.left, level+1)
            result.right = dfs(node2.right, node2.right, level+1)
            return result
        else:
            return node1 or node2



    dfs(root1, root2, 0)


    pass

if __name__ == '__main__':

    binTree1 = [1,3,2,5,None,None,None]
    binTree2 = [2,1,3,None,4,None,7]
    #배열 두개 그냥 더해서 트리 만들면 될듯

    result = solution(binTree1, binTree2)

    print('result : ' + str(result))