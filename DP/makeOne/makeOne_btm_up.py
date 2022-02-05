n = 26

d = [0] * 27

d[1]=0

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i%5==0 and d[i] > d[i//5]:
        d[i] = d[i//5] + 1
    elif i%3==0 and d[i] > d[i//3]:
        d[i] = d[i//3] + 1
    elif i%2==0 and d[i] > d[i//2]:
        d[i] = d[i//2] + 1


print(d[26])