farms = [1,3,1,5,7]

n = 4

d = [0]*100
d[1]=1
d[2]=3

for i in range(3, n+1):
    if d[i-2] + farms[i-1] > d[i-1]:
        d[i] = d[i-2] + farms[i-1]
    else:
        d[i] = d[i-1]

print(d[n])