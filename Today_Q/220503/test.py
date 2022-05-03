import sys

input=sys.stdin.readline

m,n=map(int,input().split())

parent=list(range(m+1))

def find_parent(parent,x):
    if parent[x] !=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

cnt=0

for i in range(n):
    st,ed=map(int,input().split())
    # union 하기 전인데 부모가 같다면 싸이클이 존재한다는 것
    if find_parent(parent,st)==find_parent(parent,ed):
        cnt+=1
    union_parent(parent,st,ed)
    
link=0
for i in range(1,m):
    if find_parent(parent,i)!=find_parent(parent,i+1):
        union_parent(parent,i,i+1)
        link+=1

print(cnt+link)