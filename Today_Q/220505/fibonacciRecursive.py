n=10
arr = [1,1]
dp = [0]*n

def fibonacci(n):
    if n<=1: return 1
    
    if dp[n]:
        return dp[n]

    return fibonacci(n-1) + fibonacci(n-2)

    
n = 10
a, b = 1, 1
for _ in range(n):
    b, a = b + a, b


print(fibonacci(10))

