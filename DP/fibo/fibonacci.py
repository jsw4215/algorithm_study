#TopDown

dpTable = [0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    else:
        if dpTable[x] != 0:
            return dpTable[x]
        else:
            dpTable[x] = fibo(x-1) + fibo(x-2)
            return dpTable[x]

print(fibo(99))