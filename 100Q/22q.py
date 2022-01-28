l = [200, 100, 300]

for i in reversed(range(1,3)):
    l.insert(2,i*1000)

print(l)