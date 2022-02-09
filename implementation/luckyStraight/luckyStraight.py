def solution(n):

    n = str(n)

    mid = len(n)//2

    head = n[:mid]
    tail = n[mid:]

    temp = 0
    temp2 = 0

    for i in range(mid):
        temp += int(head[i])
        temp2 += int(tail[i])

    if temp == temp2:
        print("LUCKY")
    else:
        print("READY")



if __name__ == '__main__':

    n = 7755

    solution(n)
