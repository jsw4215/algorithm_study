def solution(l):

    l.sort()

    target = 1
    
    for coin in l:
        if target < coin:
            #target+=1
            break
        
        target+=coin

    return target

if __name__ == '__main__':

    #data = list(map(int, input().split()))
    data = [3,2,1,1,9]

    res = solution(data)

    print("res", res)