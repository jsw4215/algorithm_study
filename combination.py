from itertools import combinations, permutations

house = [1,2,4,8,9]
combi = list(combinations(sorted(house), 3))

for i in combi:
    print(i)

permu = list(permutations(sorted(house)))

for i in permu:
    print(i)