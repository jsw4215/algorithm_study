import collections


def solution(root):
    if root is None:
        return 0

    queue = collections.defaultdict([root])
    depth = 0

    while queue:
        depth+=1

        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    return depth


if __name__ == '__main__':

    treeValue = [3,9,20, None, None, 15, 7]
    solution(treeValue[0])
