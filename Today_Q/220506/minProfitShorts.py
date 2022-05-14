import math


Children = [[] for _ in range(300000)]
Cost = [[0,0] for _ in range(300000)]

def traversal(node, sales):
    Cost[node][0] = 0
    Cost[node][1] = sales[node]
    
    if not Children[node]:
        return
    
    extraCost = math.inf
    for child in Children[node]:
        traversal(child, sales)
        if Cost[child][0] < Cost[child][1]:
            Cost[node][0]+=Cost[child][0]
            Cost[node][1]+=Cost[child][0]
            extraCost = min(extraCost, Cost[child][1] - Cost[child][0])
        else:
            Cost[node][0]+=Cost[child][1]
            Cost[node][1]+=Cost[child][1]
            extraCost = 0
    Cost[node][0]+=extraCost


    pass

def solution(sales, links):
    for link in links:
        Children[link[0]-1].append(link[1]-1)

    traversal(0, sales)    
    return min(Cost[0][0],Cost[0][1])

if __name__ == '__main__':

    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    res = solution(sales, links)
    print(res)
    