farms = [1,3,1,5,7]

n = 4

d = [0]*100
d[1]=1
d[2]=3


def dp_antWarriors(x):
    if x==0:
        return 0
    elif x==1:
        return d[1]
    elif x==2:
        return d[2]
    else:
        if farms[x-1] + dp_antWarriors(x-2) > dp_antWarriors(x-1):
            d[x] = farms[x-1] + dp_antWarriors(x-2)
            return d[x]
        else:
            d[x] = dp_antWarriors(x-1)
            return d[x]

result = dp_antWarriors(5)

print(result)