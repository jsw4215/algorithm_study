import collections


N = int(input())
people = list(map(int, input().split()))
sheet = collections.Counter(people)
remain = 0
groups = 0
print("sheet",sheet)
for fear, person in sorted(sheet.items()):
    print("fear, person", fear, person)
    groups += (remain+person) // fear
    remain = (remain+person) % fear
print(groups)
print("rem",remain)