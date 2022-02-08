n = [2,1]

if len(n) == 1:
    print(f'{n[0]}')

d = [0]*len(n)

d[0] = n[0]
d[1] = max(n[0],n[1])

for i in range(2,len(n)):
    if d[i-1] > n[i] + d[i-2]:
        d[i] = d[i-1]
    else:
        d[i] = n[i] + d[i-2]


print(f'{d[len(n)-1]}')