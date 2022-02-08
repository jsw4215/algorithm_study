n = 4

d = [0]*(n+1)

d[0]=1
d[1]=1

for i in range(2,n+1):
    d[i] = d[i-2] + d[i-1]

print(f'{d[n]}')