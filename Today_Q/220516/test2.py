def lim(n):
    if n==6:
        return 3
    else:
        return 3*lim(n+1)

print(lim(3))