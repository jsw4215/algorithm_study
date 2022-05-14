import sys

def twoPointer():
    
    dish = set()
    res = 0
    
    for left in range(n):

        right = left + k
        couponSushi = False

        for i in range(left, right):
            dish.add(sushi[i])

            if sushi[i]==c:
                couponSushi = True
    
        temp = len(dish)
        
        if not couponSushi:
            temp+=1
        
        res = max(temp, res)
        dish.clear()

    return res


def solution():

    #초밥을 k개만큼 연속으로 다른 초밥을 먹을 수 있는 최대값의 start, end를 찾는다.
    #1. 투포인터를 이용하여 start~end 최대값k까지 해서 다른 초밥이 놓여있는 최대 범위를 찾는다.
    #2. 해당 범위에 쿠폰 c와 같은 숫자가 없는 것이 있다면 그것과 쿠폰초밥을 더한게 정답
    
    res = twoPointer()

    return res

if __name__ == '__main__':

    n, d, k, c = map(int, sys.stdin.readline().split())

    sushi = []

    for _ in range(n):
        temp = int(sys.stdin.readline())
        sushi.append(temp)

    sushi+=sushi[:k]

    res = solution()

    print(res)