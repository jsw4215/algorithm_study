def solution(s):

    temp=int(s[0])

    for i in range(1,len(s)):
        num = int(s[i])
        if num==0 or num==1:
            temp+=num
        elif num==2 and (temp==0 or temp==1):
            temp+=num
        else:
            temp*=num

    print(f'{temp}')


if __name__ == '__main__':

    s = "02984"

    solution(s)

    # print(f'{l}')