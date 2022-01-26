#binary DFS Templates
from binary.prac import make_tree_by
from binary.structures import TreeNode


def solution(binaryTreeList1, binaryTreeList2):

    l1 = len(binaryTreeList1)
    l2 = len(binaryTreeList2)
    temp = []
    for i in range(max(l2,l1)):
        if binaryTreeList1[i] and binaryTreeList2[i]:
            temp.append(binaryTreeList1[i]+binaryTreeList2[i])
        elif binaryTreeList1[i] and binaryTreeList2[i] is None:
            temp.append(binaryTreeList1[i])
        elif binaryTreeList2[i] and binaryTreeList1[i] is None:
            temp.append(binaryTreeList2[i])
        else:
            temp.append(None)


    root = make_tree_by(temp,0)

    return root

if __name__ == '__main__':

    binTree1 = [1,3,2,5,None,None,None]
    binTree2 = [2,1,3,None,4,None,7]
    #배열 두개 그냥 더해서 트리 만들면 될듯

    result = solution(binTree1, binTree2)

    print('result : ' + str(result))