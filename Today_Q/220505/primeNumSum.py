import math
import time

def GetPrimeEratosthenes(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res

def getCasesWithPrimeNumber(prime_number, target):

    count = 0
    interval_sum = 0
    end = 0

    for start in range(len(prime_number)):
        while interval_sum < n and end < len(prime_number):
            interval_sum += prime_number[end]
            end += 1

        if interval_sum == n:
            count += 1
        interval_sum -= prime_number[start]

    return count

if __name__ == '__main__':

    n = int(input())
    
    res = GetPrimeEratosthenes(n)

    ans = getCasesWithPrimeNumber(res, n)

    print(ans)