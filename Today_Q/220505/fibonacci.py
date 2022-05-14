arr = [1,1]

def fibonacci(n):
    
    if n<=1:
        return 1

    res = n

    while n:

        arr.append(arr[-1]+arr[-2])

        n-=1

    return arr[res]

print(fibonacci(10))

