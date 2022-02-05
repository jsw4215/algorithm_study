n = 26
d=[0]*100

def dp_make1(x):

    d[x] = d[x-1] + 1

    if x%5==0 and d[x] > d[x//5]:
        print(f'{x}->')
        return dp_make1(x//5)
    elif x%3==0:
        print(f'{x}->')
        return dp_make1(x//3)
    elif x%2==0:
        print(f'{x}->')
        return dp_make1(x//2)
    else:
        if x==1:
            print(f'{x}')
            return 1

        print(f'{x}->')
        return dp_make1(x-1)

dp_make1(n)