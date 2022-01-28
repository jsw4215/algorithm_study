def longest_palindrome(target):

    palinList = []

    #start 1씩 증가
    for start in range(len(target)):
        end = len(target)

        if end-start<=1:
            break

        while (True):
            isPalin = True
            n=target[start:end]

            #문자열 짝수, 홀수 구분 로직
            odd_even_check = end-start
            if(odd_even_check%2==0):
                #짝수
                odd_even_check = False
            else:
                #홀수
                odd_even_check = True

            i=0
            j=len(n)-1

            while(True):

                if n[i]!=n[j]:
                    isPalin=False
                    break

                i+=1
                j-=1

                if odd_even_check:
                    # 홀수라면,
                    if i == j:
                        break
                else:
                    if i == j+1:
                        break

            if(isPalin):
                palinList.append(n)

            #end 1씩 감소
            end-=1
            if end-start<=1:
                break


    return palinList


if __name__ == '__main__':

    n = "sadasdfsddddddfasd"

    palinList = longest_palindrome(n)

    maximum_length=max(palinList, key=len)

    print('List : ' + str(maximum_length))