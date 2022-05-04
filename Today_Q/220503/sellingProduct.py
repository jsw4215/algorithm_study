import sys

def getProfit(customer, targetPrice):

    tot = 0

    for i in range(len(customer)):
        price = customer[i][0]
        deliveryCost = customer[i][1]

        profit = targetPrice - deliveryCost

        if price >= targetPrice and profit > 0 :
            tot+=profit

    return tot

def solution():

    sortedCustomer = sorted(customer, key= lambda x:x[0])
    
    totArr=[]

    for targetPrice in sortedCustomer:
        totArr.append(getProfit(sortedCustomer, targetPrice[0]))
    
    if sum(totArr)==0:
        return 0
    
    idx = totArr.index(max(totArr))

    res = sortedCustomer[idx][0]

    return res

if __name__ == '__main__':
    
    input = sys.stdin.readline

    n = int(input())

    customer = []

    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        customer.append(temp)

    res = solution()

    print(res)